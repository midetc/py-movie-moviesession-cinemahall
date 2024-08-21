from django.db.models import QuerySet
from db.models import MovieSession
from datetime import datetime, date


def create_movie_session(movie_show_time: datetime,
                         movie_id: int,
                         cinema_hall_id: int) -> None:
    MovieSession.objects.create(show_time=movie_show_time,
                                movie_id=movie_id,
                                cinema_hall_id=cinema_hall_id)


def get_movies_sessions(session_date: str = None) -> QuerySet:
    if session_date:
        date_obj = date.fromisoformat(session_date)
        return MovieSession.objects.filter(show_time__date=date_obj)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(session_id: int, /,
                         show_time: datetime = None,
                         movie_id: int = None,
                         cinema_hall_id: int = None):
    update_fields = []
    if show_time:
        update_fields.append("show_time")
    if movie_id:
        update_fields.append("movie_id")
    if cinema_hall_id:
        update_fields.append("cinema_hall_id")
        MovieSession.objects.filter(id=session_id).update(
            **{field: value for field, value in locals().items() if
               field in update_fields})


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
