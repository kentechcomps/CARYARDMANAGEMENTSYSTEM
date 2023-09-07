#!/home/user/.local/share/virtualenvs/CARYARDMANAGEMENTSYSTEM-cjpx4pQo/bin/ python


import click
from models import session , Vehicle

@click.group()
def cli():
    pass

# Existing Click commands

@click.command()
@click.option('--make', prompt='Vehicle Make', required=True, help='Make of the vehicle')
@click.option('--model', prompt='Vehicle Model', required=True, help='Model of the vehicle')
@click.option('--year', prompt='Vehicle Year', required=True, type=int, help='Year of the vehicle')
@click.option('--price', prompt='Vehicle Price', required=True, type=float, help='Price of the vehicle')

def add_vehicle(make, model, year, price):
    """Add a new vehicle to the database."""

    vehicle = Vehicle(make=make, model=model, year=year, price=price)
    session.add(vehicle)
    session.commit()
    click.echo('Vehicle information saved successfully!')


cli.add_command(add_vehicle)  
# # Existing Click commands
if __name__ == '__main__':
    cli()