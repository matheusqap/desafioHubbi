from celery import shared_task
from django_celery_beat.models import CrontabSchedule, PeriodicTask
import pandas as pd

from autoparts.parts.models import Part

MINIMAL_PART_QUANTITY = 10
EXTRA_QUANTITY = 10


@shared_task
def process_parts_from_dataframe(in_memory_file):
    dataframe = pd.read_csv(in_memory_file)
    parts = []

    for _, row in dataframe.iterrows():
        print(f'Processing {row['part_number']} | {row['name']}')
        parts.append(
            Part(
                part_number=row['part_number'],
                name=row['name'],
                details=row['details'],
                price=row['price'],
                quantity=row['quantity']
            )
        )

    Part.objects.bulk_create(parts)

@shared_task
def replenish_parts_quantity():
    parts = Part.objects.filter(quantity__lte=MINIMAL_PART_QUANTITY)
    for part in parts:
        print(f'Processing Quantity for Part {part.part_number}')
        parts.quantity += EXTRA_QUANTITY
        parts.save()

    
def create_periodic_tasks():
    schedule_0am, _ = CrontabSchedule.objects.get_or_create(
        minute='0', hour='0', day_of_week='*', day_of_month='*', month_of_year='*', timezone='America/Sao_Paulo'
    )
    PeriodicTask.objects.update_or_create(
        name='Process Replenish Stock',
        defaults={
            'crontab': schedule_0am,
            'task': 'autoparts.parts.tasks.replenish_parts_quantity'
        }
    )