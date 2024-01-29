from django.urls import path

from . import views

urlpatterns = [
    path('ticker/<str:ticker>', views.get_stock_data, name='get-stock-data'),
    path('recommend/', views.get_recommendation, name='get-recommendation'),

    path('<int:pk>', views.StockDetail.as_view(), name='stock-detail'),
    path('add/', views.StockCreate.as_view(), name='stock-create'),
    path('update/<int:pk>', views.StockUpdate.as_view(), name='stock-update'),
    path('delete/<int:pk>', views.StockDelete.as_view(), name='stock-delete'),

    path('portfolio/', views.PortfolioList.as_view(), name='portfolio-list'),
    path('portfolio/<int:pk>', views.PortfolioDetail.as_view(), name='portfolio-detail'),
    path('portfolio/add/<int:pk>', views.PortfolioCreate.as_view(), name='portfolio-create'),
    path('portfolio/update/<int:pk>', views.PortfolioUpdate.as_view(), name='portfolio-update'),
    path('portfolio/delete/<int:pk>', views.PortfolioDelete.as_view(), name='portfolio-delete'),

]
