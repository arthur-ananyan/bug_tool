from rest_framework.views import APIView
from .serializers import BugSerializer, CommentSerializer
from .models import Bug, Comment
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404, get_list_or_404


class BugView(APIView):

    @staticmethod
    def post(request):
        data = BugSerializer(data=request.data)

        if data.is_valid(raise_exception=True):
            bug = data.create(data.validated_data)
            return JsonResponse(data=model_to_dict(bug))

    @staticmethod
    def get(request, pk=None):
        if pk:
            bug = get_object_or_404(Bug, pk=pk)

            return JsonResponse(data=model_to_dict(bug))

        else:
            if status := request.query_params.get('status'):
                bugs = get_list_or_404(Bug.objects.filter(status=status))

                data = [model_to_dict(bug) for bug in bugs]

                return JsonResponse(data, safe=False)

            else:
                bugs = get_list_or_404(Bug)

                data = [model_to_dict(bug) for bug in bugs]

                return JsonResponse(data, safe=False)

    @staticmethod
    def put(request, pk):
        saved_bug = get_object_or_404(Bug.objects.all(), pk=pk)
        data = BugSerializer(instance=saved_bug, data=request.data, partial=True)

        if data.is_valid(raise_exception=True):
            bug = data.save()
            return JsonResponse(data=model_to_dict(bug))

    @staticmethod
    def delete(request, pk):
        bug = get_object_or_404(Bug.objects.all(), pk=pk)
        bug.delete()
        return JsonResponse({"message": f"Bug with id {pk} has been deleted"})


class CommentView(APIView):
    @staticmethod
    def post(request):
        data = CommentSerializer(data=request.data)

        if data.is_valid(raise_exception=True):
            comment = data.create(data.validated_data)
            return JsonResponse(data=model_to_dict(comment))

    @staticmethod
    def delete(request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return JsonResponse({"message": f"Comment with id {pk} has been deleted"})
