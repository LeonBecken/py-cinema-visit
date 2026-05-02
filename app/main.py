from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall
from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
    customers: list,
    hall_number: int,
    cleaner: str,
    movie: str
) -> None:
    customers_list = []
    hall = CinemaHall(hall_number)
    cleaner_object = Cleaner(cleaner)
    for customer in customers:
        customer_object = Customer(customer["name"], customer["food"])
        customers_list.append(customer_object)
        CinemaBar.sell_product(customer_object)
    hall.movie_session(movie, customers_list, cleaner_object)
