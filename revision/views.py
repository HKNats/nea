from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from user_profiles.models import Profile2
from academic.models import Topics
from .utils import LinkedList,get_unique_value_from_li

@login_required(login_url=reverse_lazy('login'))
def revision_resources(request):      
    subjects=[]
    isSubjectUpdated=False
    enrolled_subjects=Profile2.objects.filter(user_id= request.user.id)[0]
    if enrolled_subjects.subject1:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject1.subject_name,'subject_id':enrolled_subjects.subject1.id})
    if enrolled_subjects.subject2:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject2.subject_name,'subject_id':enrolled_subjects.subject2.id})
    if enrolled_subjects.subject3:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject3.subject_name,'subject_id':enrolled_subjects.subject3.id})
    if enrolled_subjects.subject4:
        isSubjectUpdated=True
        subjects.append({'subject_name':enrolled_subjects.subject4.subject_name,'subject_id':enrolled_subjects.subject4.id})
    return render(request, 'revision/list_subjects.html', {'subjects':subjects,'isSubjectUpdated':isSubjectUpdated})


 
 # used Linked list and Merged sort
@login_required(login_url=reverse_lazy('login'))
def list_topics(request,subject_id):     
    li = LinkedList()
    topics_by_subject=Topics.objects.filter(subject_id=subject_id)
    for topic in topics_by_subject:
        li.append(topic.topics_name)
    # there can be duplicate topics, to get unique value from Li, first doing merge sort and then getting unique value from Li
    li.head=li.mergeSort(li.head)  
    value=get_unique_value_from_li(li.head)
    return render(request, 'revision/list_topics.html', {'topics':value})


@login_required(login_url=reverse_lazy('login'))
def list_resources(request,topics_name):      
    resources=[]
    resources_by_topic=Topics.objects.filter(topics_name=topics_name)
    for resource in resources_by_topic:
        resources.append({'url':resource.resource_url,'resource_name':resource.resource_name})
    return render(request, 'revision/list_resources.html', {'resources':resources})