from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from . import views
from . import accounts

router = DefaultRouter()
router.register('user', views.UserViewSet)
router.register('personalSchedule', views.PersonalScheduleViewSet)
router.register('timeTable', views.TimeTableViewSet)
router.register('alarm', views.AlarmViewSet)
router.register('group', views.GroupViewSet)
router.register('groupMember', views.GroupMemberViewSet)
router.register('groupSchedule', views.GroupScheduleViewSet)
router.register('groupNotice', views.GroupNoticeViewSet)
router.register('groupBoard', views.GroupBoardViewSet)
router.register('survey', views.SurveyViewSet)
router.register('surveyQuestion', views.SurveyQuestionViewSet)
router.register('surveyAnswer', views.SurveyAnswerViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('api/oauth/', accounts.oauth, name='oauth'),
    path('api/loginKakao/', accounts.login, name='detail'),
    path('api/unlink/', accounts.unlink, name='unlink'),
    path('api/withdraw/', accounts.withdraw, name='withdraw'),
    path('api/token/', obtain_jwt_token),

    path('api/getUserGroup/<str:uid>/', views.getUserGroup.as_view()),
]