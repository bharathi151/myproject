from django.shortcuts import render

# Create your views here.
import json
from imdb.models import *
from imdb.utils import *
def home(request):
    data=Movie.objects.all()
    return render(request,'imdb_home.html',{'latest_data_list':data})

def movie(request,movie_id):
    actor={'actors':Cast.objects.filter(movie__movie_id=movie_id)}
    movie={'movies':Movie.objects.get(movie_id=movie_id)}
    actor.update(movie)
    return render(request,'imdb_movie.html',actor)

def actor(request,actor_id):
    act=Actor.objects.get(actor_id=actor_id)
    actor={'actor':act}
    movie={'movies':act.movie_set.all()}
    actor.update(movie)
    return render(request,'imdb_actor.html',actor)

def director(request,name):
    dir=Director.objects.get(name=name)
    director={'director':dir}
    movie={'movies':dir.movie_set.all()}
    director.update(movie)
    return render(request,'imdb_director.html',director)




def get_doughnut_chart_data():
    
    sql_query="""select movie.box_office_collection_in_crores from imdb_movie as movie inner join imdb_director as director on movie.director_name_id=director.id and movie.box_office_collection_in_crores>'500' and director.gender='female' limit 10;"""
    movie_collections=execute_sql_query(sql_query)
    sql_query1="""select  movie.name from imdb_movie as movie inner join imdb_director as director on movie.director_name_id=director.id and movie.box_office_collection_in_crores>'500' and director.gender='female' limit 10;"""
    movie_name=execute_sql_query(sql_query1)
    
    
    doughnut_graph_data = {
        "datasets": [{
            "data": movie_collections,
            "backgroundColor": [
                "blue",
                "orange",
                "black",
                "green"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": movie_name 
    }

    return {
        'doughnut_graph_data_one': json.dumps(doughnut_graph_data),
        'doughnut_graph_data_one_title': 'Movies directed by female director and crossed 500 crores in collections'
    }

def get_pie_chart_data():
    sql_query=""" select (100.0*count(d.gender))/(select count(*) from imdb_movie as m1) from imdb_director as d inner join imdb_movie as m on m.director_name_id=d.id group by d.gender order by d.gender desc;"""
    count_of_movies=execute_sql_query(sql_query)
    pie_chart_data = {
        "datasets": [{
            "data": list(count_of_movies),
            "backgroundColor": [
                "red",
                "green",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ],
            "hoverBackgroundColor": [
                "rgba(0, 123, 255,0.9)",
                "rgba(0, 123, 255,0.7)",
                "rgba(0, 123, 255,0.5)",
                "rgba(0,0,0,0.07)"
            ]

        }],
        "labels": ["Male","Female"]
    }

    return {
        'pie_chart_data_one': json.dumps(
            pie_chart_data),
        'pie_chart_data_one_title': 'percentage of movies directed by male and female directors'
    }


def get_one_bar_plot_data():
    sql_query="""select avg(movie.box_office_collection_in_crores) from imdb_movie as movie group by movie.year_of_release;"""
    movie_collections=execute_sql_query(sql_query)
    sql_query1="""select  movie.year_of_release from imdb_movie as movie group by movie.year_of_release;"""
    movie_year=execute_sql_query(sql_query1)
    
    
    single_bar_chart_data = {
        "labels": movie_year,
        "datasets": [{
            "data": movie_collections,
            "name": "Single Bar Chart",
            "label":"avg_collections",
            "borderColor": "rgba(0, 123, 255, 0.9)",
            "border_width": "0",
            "backgroundColor": "rgba(0, 123, 255, 0.5)"
        }]
    }
    return {
        'single_bar_chart_data_one': json.dumps(single_bar_chart_data),
        'single_bar_chart_data_one_title': 'Average collections movies yearly'
    }



    
def analytics(request):
    polar_chart=get_area_plot_data()

    
    one=get_one_bar_plot_data()
    polar_chart.update(one)

    doughnut_graph=get_doughnut_chart_data()
    polar_chart.update(doughnut_graph)
    
    pie=get_pie_chart_data()
    polar_chart.update(pie)
    # two=get_two_bar_plot_data()
    # # line=get_two_bar_plot_data()
    # polar_chart.update(two)
    print(polar_chart)
    return render(request,'analytics.html',context=polar_chart)
