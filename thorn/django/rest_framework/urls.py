"""DRF URL dispatch table.

Usage
=====

To include the rest-framework API views in your project use the
:meth:`django.conf.urls.include` function, with a proper namespace argument:

.. code-block:: python

    from django.conf.urls.include import include, url

    urlpatterns = [
        url(r'^hooks/',
            include(('thorn.django.rest_framework.urls', 'thorn'),
                    namespace='webhook')),
    ]

Endpoints
=========

Two new API endpoints will now be available in your application:

- ``GET /hooks/``

    List of webhook subscriptions related to the currently logged in user.

- ``POST /hooks/``

    Create new subscription owned by the currently logged in user.

- ``GET /hooks/<uuid>/``

    Get detail about specific subscription by unique identifier (uuid).

- ``POST|PATCH /hook/<uuid>/``

    Update subscription given its unique identifier (uuid).

- ``DELETE /hook/<uuid>/``

    Delete subscription given its unique identifier (uuid).
"""


from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.SubscriberList.as_view(), name='list'),
    path('<uuid:uuid>/',
         views.SubscriberDetail.as_view(), name='detail'),
]
