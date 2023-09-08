import click
from models import session, Customer  # Import your SQLAlchemy session and Customer model

@click.group()
def cli():
    pass

# Existing Click commands

@click.command()
@click.option('--name', prompt='Enter Name', required=True, help='Name of the customer')
@click.option('--email', prompt='Enter Email', required=True, help='Email of the customer')
@click.option('--phone-number', prompt='Enter Phone Number', required=True, type=int, help='Phone number of the customer')
def add_customer(name, email, phone_number):
    """Add a new customer to the database."""
    customer = Customer(name=name, email=email, phone=phone_number)
    session.add(customer)
    session.commit()
    click.echo('Customer information submitted successfully!')

cli.add_command(add_customer)

if __name__ == '__main__':
    cli()

