
from django.urls import path, re_path
from . import views





urlpatterns = [

    path("update_server/", views.git_pythonanywhere, name="update"),

    path('pdf_viewer1', views.pdf_viewer1, name='pdf-viewer1'),

    # path('pdf_view/<int:pk>', views.render_pdf_view, name='pdf-view'),
    
    
    path('loginpage', views.loginPage, name='login_user'),
    path('logout', views.logoutUser, name='logout'),
    path('register_user', views.register_user, name='register_user'),

    path('userhomepage', views.userHomepage, name='user-homepage'),
    path('form_view_error', views.form_view_error, name='form_view_error'),

    path('', views.welcome, name='welcome'),

    path('step1_page', views.form_one_page, name='step1_page'),
    path('step1', views.Step1_Form_Completion, name='step1'),
    path('form_view/<step_one>', views.Step1_Form_View, name='form_view'),
    path('edit/<step_one>', views.editpost, name='editpost'),
    path('delete/<step_one>', views.Step1_Form_Delete, name='delete-post'),

    path('step2_page', views.form_two_page, name='step2_page'),
    path('step2', views.Step2_Form_Completion, name='step2'),
    path('form_view2', views.Step2_Form_View, name='form_view2'),
    path('edit2/<step_two>', views.editpost2, name='editpost2'),
    path('delete2/<step_two>', views.Step2_Form_Delete, name='delete-post2'),

    path('step3_page', views.form_three_page, name='step3_page'),
    path('step3', views.Step3_Form_Completion, name='step3'),
    path('form_view3', views.Step3_Form_View, name='form_view3'),
    path('edit3/<step_three>', views.editpost3, name='editpost3'),
    path('delete3/<step_three>', views.Step3_Form_Delete, name='delete-post3'),

    path('step4_page', views.form_four_page, name='step4_page'),
    path('step4', views.Step4_Form_Completion, name='step4'),
    path('form_view4', views.Step4_Form_View, name='form_view4'),
    path('edit4/<step_four>', views.editpost4, name='editpost4'),
    path('delete4/<step_four>', views.Step4_Form_Delete, name='delete-post4'),

    path('step5_page', views.form_five_page, name='step5_page'),
    path('step5', views.Step5_Form_Completion, name='step5'),
    path('form_view5', views.Step5_Form_View, name='form_view5'),
    path('edit5/<step_five>', views.editpost5, name='editpost5'),
    path('delete5/<step_five>', views.Step5_Form_Delete, name='delete-post5'),

    path('step6_page', views.form_six_page, name='step6_page'),
    path('step6', views.Step6_Form_Completion, name='step6'),
    path('form_view6', views.Step6_Form_View, name='form_view6'),
    path('edit6/<step_six>', views.editpost6, name='editpost6'),
    path('delete6/<step_six>', views.Step6_Form_Delete, name='delete-post6'),

    path('step7_page', views.form_seven_page, name='step7_page'),
    path('step7', views.Step7_Form_Completion, name='step7'),
    path('form_view7', views.Step7_Form_View, name='form_view7'),
    path('edit7/<step_seven>', views.editpost7, name='editpost7'),
    path('delete7/<step_seven>', views.Step7_Form_Delete, name='delete-post7'),

    path('step8_page', views.form_eight_page, name='step8_page'),
    path('step8', views.Step8_Form_Completion, name='step8'),
    path('form_view8', views.Step8_Form_View, name='form_view8'),
    path('edit8/<step_eight>', views.editpost8, name='editpost8'),
    path('delete8/<step_eight>', views.Step8_Form_Delete, name='delete-post8'),


    path('base', views.base, name='base'),
    path('shell_test', views.shellTesting, name='shell_test'),
]




