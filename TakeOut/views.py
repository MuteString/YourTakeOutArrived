from django.shortcuts import render, render_to_response


def index(requet):
    return render_to_response('base.html')
