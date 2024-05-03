from rest_framework.pagination import PageNumberPagination


class EventPagination(PageNumberPagination):
    page_size: int = 10
    page_size_query_param: str = 'event_page_size'
    max_page_size: int = 1000
    page_query_param: str = 'event_page'


class AttendeePagination(PageNumberPagination):
    page_size_query_param: str = 'attendee_page_size'
    max_page_size: int = 100
    page_query_param: str = 'attendee_page'