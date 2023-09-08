import click
from models import session, Customer ,Review  # Import your SQLAlchemy session and Customer model

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

@click.command()
def list_customers():
    """List all your customers from the database."""
    
    try:
        # Query the database to get all vehicles
        customers = session.query(Customer).all()

        if not customers:
            click.echo("You don't have any customers in the database.")
        else:
            # Display the list of vehicles
            click.echo("List of your Customers:")
            for customer in customers:
                click.echo(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}, Phone: {customer.phone}")

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
        
cli.add_command(list_customers)

@click.command()
@click.option('--customer-id', prompt='Customer ID', required=True, type=int, help='ID of the customer adding the review')
@click.option('--rating', prompt='Rating (1-5)', required=True, type=int, help='Rating for the review (1-5)')
@click.option('--comment', prompt='Comment', required=True, help='Comment for the review')

def add_review(customer_id, rating, comment):
    """Add a review to the database."""

    try:
        # Query the database to find the customer by ID
        customer = session.query(Customer).filter_by(id=customer_id).first()

        if not customer:
            click.echo(f"Customer with ID {customer_id} not found in the database.")
        else:
            # Create a new review and associate it with the customer
            review = Review(star_rating=rating, comment=comment, customer=customer)
            session.add(review)
            session.commit()
            click.echo('Review submitted successfully.')

    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
cli.add_command(add_review)
if __name__ == '__main__':
    cli()

