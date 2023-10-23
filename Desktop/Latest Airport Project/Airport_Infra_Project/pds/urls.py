from django.urls import path, re_path
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.decorators import login_required
from django.views.static import serve
from django.conf import settings

from . import views, hrViews,hrViews2, otherViews, PayslipViews, deleteViews, xcelViews , payrollViews , AANSOOViews, ADMSViews, ANSViews, ATSViews, CATCViews, CSISViews, ELSViews, FICGViews, FMDViews, FSISViews, IASViews, ODGViews, OFSAMViews, ADMINViews, leaveViews, regularXcelViews, PrintViews, separateViews, PostViews, QRViews
from .views import SignUpView


app_name = 'pds' 
urlpatterns = [
# Admin
    # Admin Dashboard
    path('hr', hrViews.Dashboard, name='Dashboard'),
# Employees list
    # path('permanent', hrViews.Permanent, name='Permanent'),
    # path('jo', hrViews.JO, name='JO'),
    # path('os', hrViews.Outsourced, name='os'),
    # path('coterm', hrViews.Coterm, name='Coterm'),
    # path('consultant', hrViews.Consultant, name='Consultant'),
    # path('separated', hrViews.Separated, name='Separated'),
    # path('for-approval', hrViews.ForApproval, name='ForApproval'),
    # Vaccine Admin Show
    # path('vax', hrViews.VaccineAdminShow, name='VaccineAdminShow'),
    # path('vax_show', hrViews.VaccineAdminDisplay, name='VaccineAdminDisplay'),
    # Index page
    path('', views.index, name='index'),
    # Account Sign Up
    path('signup', SignUpView.as_view(), name="signup"),
    # Account settings
    path('settings/', otherViews.Settings, name="settings"),
    # Home page after Login
    path('home/',views.home,name="home"),
    # ex: /pds/personalinfo/
    path('<int:id>/', views.PersonalDetail, name='PersonalDetail'),

# Search Filter
    # path('saerchpermanent', hrViews.SearchPermanent, name='SearchPermanent'),
    # path('permanentfilter', hrViews.PermanentFilter, name='PermanentFilter'),
    # path('jofilter', hrViews.JOFilter, name='JOFilter'),
    # path('outsourcefilter', hrViews.OutsourcedFilter, name='OutsourcedFilter'),
    # path('cotermfilter', hrViews.CotermFilter, name='CotermFilter'),
    # path('consultantfilter', hrViews.ConsultantFilter, name='ConsultantFilter'),
    # path('sefilter', hrViews.SEFilter, name='SEFilter'),
    # path('fafilter', hrViews.FAFilter, name='FAFilter'),

# PDS sheet
     path('sheet1/',views.Page1,name="Page1"),
     path('sheet2/',views.Page2,name="Page2"),
     path('sheet3/',views.Page3,name="Page3"),
     path('sheet4/',views.Page4,name="Page4"),
     path('separate1/',separateViews.Separate1,name="Separate1"),
     path('separate2/',separateViews.Separate2,name="Separate2"),

# PDS sheet HR
     # path('page1/<int:id>',hrViews.Page1,name="HrPage1"),
     # path('page2/<int:id>',hrViews.Page2,name="HrPage2"),
     # path('page3/<int:id>',hrViews.Page3,name="HrPage3"),
     # path('page4/<int:id>',hrViews.Page4,name="HrPage4"),

# Personal Information
    # ex: /pds/personal/
    path('personalinfo', views.PersonalPDS, name='PersonalPDS'),
    path('personalinfo1', views.PersonalPDS1, name='PersonalPDS1'),
    path('personalinfo2', views.PersonalPDS2, name='PersonalPDS2'),
    path('personalinfo3', views.PersonalPDS3, name='PersonalPDS3'),
    path('personalinfo4', views.PersonalPDS4, name='PersonalPDS4'),
    # Create Personal Info
    path('infoCreate', views.InfoCreate, name='InfoCreate'),
    # Edit Personal Info
    path('infoEdit/<int:id>', views.InfoEdit, name='InfoEdit'),
    # Update Personal Info
    path('infoUpdate/<int:id>', views.InfoUpdate, name='InfoUpdate'),
    # ex: /pds/photo/
    path('photoUpload/<int:id>', views.PhotoUpload, name='PhotoUpload'),
    # ex: /pds/photo/
    path('photoUpdate/<int:id>', views.PhotoUpdate, name='PhotoUpdate'),
# Children Information
    # ex: /pds/children/  Add Children
    path('childrenCreate', views.ChildrenlCreate, name='ChildrenlCreate'),
# Education Information
    # ex: /pds/education/  Add Education
    path('educationCreate', views.EducationCreate, name='EducationCreate'),
# Eligibility Information
    # ex: /pds/childress/  Add Eligibility
    path('eligibilityCreate', views.EligibilityCreate, name='EligibilityCreate'),
# Experience Information
    # ex: /pds/experienceCreate  Add Experience
    path('experienceCreate', views.ExperienceCreate, name='ExperienceCreate'),
# Voluntary Information
    # ex: /pds/voluntaryCreate  Add Voluntary
    path('voluntaryCreate', views.VoluntaryCreate, name='VoluntaryCreate'),
#Learning  Information
    # ex: /pds/otherinfoCreate  Add Learning
    path('learningCreate', views.LearningCreate, name='LearningCreate'),
#Otherinfo  Information
    # ex: /pds/otherinfo/create  Add Otherinfo
    path('otherinfoCreate', views.OtherinfoCreate, name='OtherinfoCreate'),
# Refferences Information
    # ex: /pds/refferencesCreate  Add Refferences
    path('refferencesCreate', views.RefferencesCreate, name='RefferencesCreate'),
 #Learning  Information
    # ex: /pds/skillsCreate Add Learning
    path('skillsCreate', views.SkillsCreate, name='SkillsCreate'),
#Otherinfo  Information
    # ex: /pds/recognitionsCreate  Add Otherinfo
    path('recognitionsCreate', views.RecognitionsCreate, name='RecognitionsCreate'),
# Refferences Information
    # ex: /pds/membershipCreate  Add Refferences
    path('membershipCreate', views.MembershipCreate, name='MembershipCreate'),




# EDIT views
        # Permanent Edit
    # path('itemEdit/<int:id>', hrViews.PermanentItemEdit, name='PermanentItemEdit'),
    #     # Status Edit
    # path('statusEdit/<int:id>', hrViews.StatusEdit, name='StatusEdit'),
    #     # Data Edit
    # path('dataEdit/<int:id>', hrViews.DataEdit, name='DataEdit'),
    #     # PDS Status Edit
    # path('approvalEdit/<int:id>', hrViews.ForApprovalEdit, name='ForApprovalEdit'), 
    #     # Edit Position
    # path('positionEdit/<int:id>', hrViews.PositionEdit, name='PositionEdit'),
    #     # Edit Office
    # path('officeEdit/<int:id>', hrViews.OfficeEdit, name='OfficeEdit'),
        # Edit Child Info
    path('childEdit/<int:id>', views.ChildEdit, name='ChildEdit'),
        # Edit Personal Info
    path('educationEdit/<int:id>', views.EducationEdit, name='EducationEdit'),
        # Edit Personal Info
    path('eligibilityEdit/<int:id>', views.EligibilityEdit, name='EligibilityEdit'),
        # Edit Personal Info
    path('experienceEdit/<int:id>', views.ExperienceEdit, name='ExperienceEdit'),
        # Edit Personal Info
    path('voluntaryEdit/<int:id>', views.VoluntaryEdit, name='VoluntaryEdit'),
        # Edit Personal Info
    path('learningEdit/<int:id>', views.LearningEdit, name='LearningEdit'),
        # Edit Personal Info
    path('otherinfoEdit/<int:id>', views.OtherinfoEdit, name='OtherinfoEdit'),
        # Edit Personal Info
    path('skillsEdit/<int:id>', views.SkillsEdit, name='SkillsEdit'),
        # Edit Personal Info
    path('recognitionsEdit/<int:id>', views.RecognitionsEdit, name='RecognitionsEdit'),
        # Edit Personal Info
    path('membershipEdit/<int:id>', views.MembershipEdit, name='MembershipEdit'),
       # Edit Personal Info
    path('refferencesEdit/<int:id>', views.RefferencesEdit, name='RefferencesEdit'),

# Delete views
        # Delete Child Info
    path('childDelete/<int:id>', deleteViews.ChildDelete, name='ChildDelete'),
        # Delete Personal Info
    path('educationDelete/<int:id>', deleteViews.EducationDelete, name='EducationDelete'),
        # Delete Personal Info
    path('eligibilityDelete/<int:id>', deleteViews.EligibilityDelete, name='EligibilityDelete'),
        # Delete Personal Info
    path('experienceDelete/<int:id>', deleteViews.ExperienceDelete, name='ExperienceDelete'),
        # Delete Personal Info
    path('voluntaryDelete/<int:id>', deleteViews.VoluntaryDelete, name='VoluntaryDelete'),
        # Delete Personal Info
    path('learningDelete/<int:id>', deleteViews.LearningDelete, name='LearningDelete'),
        # Delete Personal Info
    path('skillsDelete/<int:id>', deleteViews.SkillsDelete, name='SkillsDelete'),
        # Delete Personal Info
    path('recognitionsDelete/<int:id>', deleteViews.RecognitionsDelete, name='RecognitionsDelete'),
        # Delete Personal Info
    path('membershipDelete/<int:id>', deleteViews.MembershipDelete, name='MembershipDelete'),
       # Delete Personal Info
    path('refferencesDelete/<int:id>', deleteViews.RefferencesDelete, name='RefferencesDelete'),
       # Delete Personal Info
    path('payrollDelete/<int:id>', deleteViews.PayrollDelete, name='PayrollDelete'),
       # Delete Personal Info
    path('bonusDelete/<int:id>', deleteViews.BonusDelete, name='BonusDelete'),



# Update views
        # Permanent Update
    # path('itemUpdate/<int:id>', hrViews.PermanentItemUpdate, name='PermanentItemUpdate'),
    #     # Status Update
    # path('statusUpdate/<int:id>', hrViews.StatusUpdate, name='StatusUpdate'),
    #      # Data Update
    # path('dataUpdate/<int:id>', hrViews.DataUpdate, name='DataUpdate'),
    #     # PDS Status Update
    # path('approvalUpdate/<int:id>', hrViews.ForApprovalUpdate, name='ForApprovalUpdate'),
    #     # Position Update
    # path('positionUpdate/<int:id>', hrViews.PositionUpdate, name='PositionUpdate'),
    #     # Office Update
    # path('officeUpdate/<int:id>', hrViews.OfficeUpdate, name='OfficeUpdate'),
        # Edit Children Info
    path('childUpdate/<int:id>', views.ChildUpdate, name='ChildUpdate'),
        # Edit Personal Info
    path('educationUpdate/<int:id>', views.EducationUpdate, name='EducationUpdate'),
        # Edit Personal Info
    path('eligibilityUpdate/<int:id>', views.EligibilityUpdate, name='EligibilityUpdate'),
        # Edit Personal Info
    path('experienceUpdate/<int:id>', views.ExperienceUpdate, name='ExperienceUpdate'),
        # Edit Personal Info
    path('voluntaryUpdate/<int:id>', views.VoluntaryUpdate, name='VoluntaryUpdate'),
        # Edit Personal Info
    path('learningUpdate/<int:id>', views.LearningUpdate, name='LearningUpdate'),
        # Edit Personal Info
    path('otherinfoUpdate/<int:id>', views.OtherinfoUpdate, name='OtherinfoUpdate'),
        # Edit Personal Info
    path('skillsUpdate/<int:id>', views.SkillsUpdate, name='SkillsUpdate'),
        # Edit Personal Info
    path('recognitionsUpdate/<int:id>', views.RecognitionsUpdate, name='RecognitionsUpdate'),
        # Edit Personal Info
    path('membershipUpdate/<int:id>', views.MembershipUpdate, name='MembershipUpdate'),
       # Edit Personal Info
    path('refferencesUpdate/<int:id>', views.RefferencesUpdate, name='RefferencesUpdate'),

# Post Modules
    # Post Create 
    # path('post', PostViews.Index, name='postIndex'),
    # # Post Create
    # path('postCreate', PostViews.PostCreate, name='postCreate'),
    # # Post Edit
    # path('postEdit/<int:id>', PostViews.PostEdit, name='PostEdit'),
    # # Post Update
    # path('postUpdate/<int:id>', PostViews.PostUpdate, name='PostUpdate'),
    # # Post Update
    # path('postDelete/<int:id>', deleteViews.DeletePost, name='DeletePost'),
    # Announcement
    path('announcement', PostViews.Announcement, name='Announcement'),
    # Reorg Announcement
    path('reorg', PostViews.Reorg, name='Reorg'),
    # QNA Reorg
    path('qna', PostViews.QnA, name='QnA'),
    # NotifyTrainng
    path('notify_training', PostViews.NotifyTraining, name = 'notify_training'),
    # NotifyTrainng List
    path('notify-training', otherViews.TrainingRecordNotif, name = 'notify-training'),

# Other Modules
    # Vaccine Create
    path('vaxCreate', otherViews.VaccineCreate, name='vaxCreate'),
    # Vaccine Show
    path('vaccine', otherViews.VaccineShow, name='VaccineShow'),
    # Vaccine Update
    path('updateVax/<int:id>', otherViews.VaccineUpdate, name='vax_update'),


# Other Modules
    # Vaccine Create
    path('vaxCreate', otherViews.VaccineCreate, name='vaxCreate'),
    # Training Show
    path('trainings/<int:id>', otherViews.TrainingRecord, name='training_record'),
    # Create Training
    path('createTrainings/<int:id>', otherViews.CreateTrainingRecord, name='create_training_record'),
    # Edit Training
    path('editTrainings/<int:id>', otherViews.EditTrainingRecord, name='edit_training_record'),
    # Delete Training
    path('deleteTrainings/<int:id>', otherViews.DeleteTrainingRecord, name='delte_training_record'),
    # Education Show
    path('education/<int:id>', otherViews.EducationList, name='education_list'),
    # Eligibility Show
    path('eligibility/<int:id>', otherViews.EligibilityList, name='eligibility_list'),
    # Salary Grade
    path('sg', otherViews.SalaryGradeView, name='salary_grade'),
    # Salary Grade ADD
    path('sg_create', otherViews.SalaryGradeCreate, name='salary_grade_create'),
     # Salary Grade EDIT
    path('sg_edit/<int:id>', otherViews.SalaryGradeEdit, name='salary_grade_edit'),
     # Salary Grade UPDATE
    path('sg_update/<int:id>', otherViews.SalaryGradeUpdate, name='salary_grade_update'),
    # Position
    path('position', otherViews.PositionView, name='position'),
    # Position Grade ADD
    path('position_create', otherViews.PositionCreate, name='position_create'),
     # Position  EDIT
    path('position_edit/<int:id>', otherViews.PositionEdit, name='position_edit'),
     # Position  UPDATE
    path('position_update/<int:id>', otherViews.PositionUpdate, name='position_update'),
    # Signatory
    path('sign', otherViews.SignatoryView, name='sign'),
     # Signatory  EDIT
    path('sign_edit/<int:id>', otherViews.SignatoryEdit, name='signatory_edit'),
     # Signatory  UPDATE
    path('sign_update/<int:id>', otherViews.SignatoryUpdate, name='signatory_update'),


# HRMD Payroll
    # Payroll Index View
    # path('payroll', hrViews.CaapPayroll, name='caap_payroll'),
    # # Payroll Create View
    # path('createPayroll', hrViews.CreatePayroll, name='create_payroll'),
    # # Payroll Edit View
    # path('editPayroll/<int:id>', hrViews.EditPayroll, name='edit_payroll'),
    # # View Users
    # path('users_list', hrViews.UsersView, name='users_hr'),
    # # Edit Users
    # path('usersEdit/<int:id>', hrViews.UsersEdit, name='usersEdit'),
    # # Update Users
    # path('usersUpdate/<int:id>', hrViews.UsersUpdate, name='usersUpdate'),
    # # OFFICE LIST Payroll
    # path('payroll_list', payrollViews.PayrollPerOffice, name='PayrollPerOffice'),
    # # No PDS
    # path('createPayroll2', hrViews2.CreatePayroll, name='create_payroll'),
    # # Payroll Edit View
    # path('editPayroll2/<int:id>', hrViews2.EditPayroll, name='edit_payroll'),


# Leave Credits
    # Leave Index View
    # path('leave/<int:id>', leaveViews.leaveView, name='leave_view'),
    # # Leave Create Page
    # path('createLeave/<int:id>', leaveViews.leaveCreate, name='leave_create'),
    # # Leave Update Page
    # path('updateLeave/<int:id>', leaveViews.leaveUpdate, name='leave_update'),
    # # SPFLeave Create Page
    # path('createSPFLeave/<int:id>', leaveViews.SPFLeaveCreate, name='spfleave_create'),
    #  # SPFLeave Update Page
    # path('updateSPFLeave/<int:id>', leaveViews.SPFLeaveUpdate, name='spfleave_update'),
    # # Delete Leave Create Page
    # path('deleteLeave/<int:id>', leaveViews.DeleteLeave, name='leave_delete'),

     # Leave Credits View
    path('leavecredits', leaveViews.leaveCredits, name='leave_credits'),

# Monthly Payslip
    path('view_payslip',PayslipViews.ViewPayslip, name='view_payslip'),
    path('view_january',PayslipViews.ViewJanuary, name='view_january'),
    path('view_february',PayslipViews.ViewFebruary, name='view_february'),
    path('view_march',PayslipViews.ViewMarch, name='view_march'),
    path('view_april',PayslipViews.ViewApril, name='view_april'),
    path('view_may',PayslipViews.ViewMay, name='view_may'),
    path('view_june',PayslipViews.ViewJune, name='view_june'),
    path('view_july',PayslipViews.ViewJuly, name='view_july'),
    path('view_august',PayslipViews.ViewAugust, name='view_august'),
    path('view_september',PayslipViews.ViewSeptember, name='view_september'),
    path('view_october',PayslipViews.ViewOctober, name='view_october'),
    path('view_november',PayslipViews.ViewNovember, name='view_november'),
    path('view_december',PayslipViews.ViewDecember, name='view_december'),

# Monthly Payslip For HR
    # path('hr_view_payslip/<int:id>',PayslipViews.HRViewPayslip, name='hr_view_payslip'),
    # path('hr_view_january/<int:id>',PayslipViews.HRViewJanuary, name='hr_view_january'),
    # path('hr_view_february/<int:id>',PayslipViews.HRViewFebruary, name='hr_view_february'),
    # path('hr_view_march/<int:id>',PayslipViews.HRViewMarch, name='hr_view_march'),
    # path('hr_view_april/<int:id>',PayslipViews.HRViewApril, name='hr_view_april'),
    # path('hr_view_may/<int:id>',PayslipViews.HRViewMay, name='hr_view_may'),
    # path('hr_view_june/<int:id>',PayslipViews.HRViewJune, name='hr_view_june'),
    # path('hr_view_july/<int:id>',PayslipViews.HRViewJuly, name='hr_view_july'),
    # path('hr_view_august/<int:id>',PayslipViews.HRViewAugust, name='hr_view_august'),
    # path('hr_view_september/<int:id>',PayslipViews.HRViewSeptember, name='hr_view_september'),
    # path('hr_view_october/<int:id>',PayslipViews.HRViewOctober, name='hr_view_october'),
    # path('hr_view_november/<int:id>',PayslipViews.HRViewNovember, name='hr_view_november'),
    # path('hr_view_december/<int:id>',PayslipViews.HRViewDecember, name='hr_view_december'),

# Payroll Per Office
    # path('aansoo_payroll',payrollViews.AANSOOPayroll, name='aansoo_payroll'),
    # path('adms_payroll',payrollViews.ADMSPayroll, name='adms_payroll'),
    # path('ans_payroll',payrollViews.ANSPayroll, name='ans_payroll'),
    # path('ats_payroll',payrollViews.ATSPayroll, name='ats_payroll'),
    # path('catc_payroll',payrollViews.CATCPayroll, name='catc_payroll'),
    # path('csis_payroll',payrollViews.CSISPayroll, name='csis_payroll'),
    # path('els_payroll',payrollViews.ELSPayroll, name='els_payroll'),
    # path('ficg_payroll',payrollViews.FICGPayroll, name='ficg_payroll'),
    # path('fmd_payroll',payrollViews.FMDPayroll, name='fmd_payroll'),
    # path('fsis_payroll',payrollViews.FSISPayroll, name='fsis_payroll'),
    # path('ias_payroll',payrollViews.IASPayroll, name='ias_payroll'),
    # path('odg_payroll',payrollViews.ODGPayroll, name='odg_payroll'),
    # path('ofsam_payroll',payrollViews.OFSAMPayroll, name='ofsam_payroll'),
    # path('admin_payroll',payrollViews.ADMINPayroll, name='admin_payroll'),

# Payslip Per Office Nov
#     path('aansoo_payroll_nov',PayslipViews.AANSOOPayslipNov, name='aansoo_nov'),
#     path('adms_payroll_nov',PayslipViews.ADMSPayslipNov, name='adms_nov'),
#     path('ans_payroll_nov',PayslipViews.ANSPayslipNov, name='ans_nov'),
#     path('ats_payroll_nov',PayslipViews.ATSPayslipNov, name='ats_nov'),
#     path('catc_payroll_nov',PayslipViews.CATCPayslipNov, name='catc_nov'),
#     path('csis_payroll_nov',PayslipViews.CSISPayslipNov, name='csis_nov'),
#     path('els_payroll_nov',PayslipViews.ELSPayslipNov, name='els_nov'),
#     path('ficg_payroll_nov',PayslipViews.FICGPayslipNov, name='ficg_nov'),
#     path('fmd_payroll_nov',PayslipViews.FMDPayslipNov, name='fmd_nov'),
#     path('fsis_payroll_nov',PayslipViews.FSISPayslipNov, name='fsis_nov'),
#     path('ias_payroll_nov',PayslipViews.IASPayslipNov, name='ias_nov'),
#     path('odg_payroll_nov',PayslipViews.ODGPayslipNov, name='odg_nov'),
#     path('ofsam_payroll_nov',PayslipViews.OFSAMPayslipNov, name='ofsam_nov'),
#     path('admin_payroll_nov',PayslipViews.ADMINPayslipNov, name='admin_nov'),
# # Bonus Views
#     path('bonuses', PayslipViews.BonusesPage, name='Bonuses'),
#     path('editBonus/<int:id>', PayslipViews.EditBonus, name='editBonus'),
#     path('editBonus2/<int:id>', PayslipViews.EditBonus2, name='editBonus2'),
#     path('createBonus', PayslipViews.CreateBonus, name='createBonus'),
#     path('createBonus2', PayslipViews.CreateBonus2, name='createBonus2'),


    # privacy page
    path('privacy', otherViews.PrivacyPage, name='privacy_page'),

    # help page
    path('help', otherViews.HelpPage, name='help_page'),

    # Frequently Answered Questions page
    path('faq', otherViews.FAQPage, name='faq_page'),

# export File
    # path('exportUser', xcelViews.export_users_xls, name='export_users_xls'),
    # path('exportPermanent', regularXcelViews.export_permanents_xls, name='export_permanents_xls'),
    # path('exportOutsourced', regularXcelViews.Export_Outsourced_Xls, name='export_Outsourced_xls'),
    # path('exportPayroll', xcelViews.export_payroll_xls, name='export_payroll_xls'),
    # path('exportPayroll2', xcelViews.export_payroll2_xls, name='export_payroll2_xls'),

# View PDF
#     path('aansoo_pdf_view/', AANSOOViews.ViewPDF.as_view(), name="aansoo_view"),
#     path('adms_pdf_view/', ADMSViews.ViewPDF.as_view(), name="adms_view"),
#     path('ans_pdf_view/', ANSViews.ViewPDF.as_view(), name="ans_view"),
#     path('ats_pdf_view/', ATSViews.ViewPDF.as_view(), name="ats_view"),
#     path('catc_pdf_view/', CATCViews.ViewPDF.as_view(), name="catc_view"),
#     path('csis_pdf_view/', CSISViews.ViewPDF.as_view(), name="csis_view"),
#     path('els_pdf_view/', ELSViews.ViewPDF.as_view(), name="els_view"),
#     path('ficg_pdf_view/', FICGViews.ViewPDF.as_view(), name="ficg_view"),
#     path('fmd_pdf_view/', FMDViews.ViewPDF.as_view(), name="fmd_view"),
#     path('fsis_pdf_view/', FSISViews.ViewPDF.as_view(), name="fsis_view"),
#     path('ias_pdf_view/', IASViews.ViewPDF.as_view(), name="ias_view"),
#     path('odg_pdf_view/', ODGViews.ViewPDF.as_view(), name="odg_view"),
#     path('ofsam_pdf_view/', OFSAMViews.ViewPDF.as_view(), name="ofsam_view"),
#     path('admin_pdf_view/', ADMINViews.ViewPDF.as_view(), name="admin_view"),

# # View PDF
#     path('aansoo_pdf_view_legal/', AANSOOViews.ViewPDFLegal.as_view(), name="aansoo_view_legal"),
#     path('adms_pdf_view_legal/', ADMSViews.ViewPDFLegal.as_view(), name="adms_view_legal"),
#     path('ans_pdf_view_legal/', ANSViews.ViewPDFLegal.as_view(), name="ans_view_legal"),
#     path('ats_pdf_view_legal/', ATSViews.ViewPDFLegal.as_view(), name="ats_view_legal"),
#     path('catc_pdf_view_legal/', CATCViews.ViewPDFLegal.as_view(), name="catc_view_legal"),
#     path('csis_pdf_view_legal/', CSISViews.ViewPDFLegal.as_view(), name="csis_view_legal"),
#     path('els_pdf_view_legal/', ELSViews.ViewPDFLegal.as_view(), name="els_view_legal"),
#     path('ficg_pdf_view_legal/', FICGViews.ViewPDFLegal.as_view(), name="ficg_view_legal"),
#     path('fmd_pdf_view_legal/', FMDViews.ViewPDFLegal.as_view(), name="fmd_view_legal"),
#     path('fsis_pdf_view_legal/', FSISViews.ViewPDFLegal.as_view(), name="fsis_view_legal"),
#     path('ias_pdf_view_legal/', IASViews.ViewPDFLegal.as_view(), name="ias_view_legal"),
#     path('odg_pdf_view_legal/', ODGViews.ViewPDFLegal.as_view(), name="odg_view_legal"),
#     path('ofsam_pdf_view_legal/', OFSAMViews.ViewPDFLegal.as_view(), name="ofsam_view_legal"),
#     path('admin_pdf_view_legal/', ADMINViews.ViewPDFLegal.as_view(), name="admin_view_legal"),

# # QR Code
    # path('qrcode', QRViews.QRCode, name='qrcode'),
    # path('qr_ans', QRViews.QR_ANS, name='qr_ans'),
    # path('qr_ats', QRViews.QR_ATS, name='qr_ats'),
    # path('qr_afs', QRViews.QR_AFS, name='qr_afs'),
    # path('qr_fsis', QRViews.QR_FSIS, name='qr_fsis'),
    # path('qr_odg', QRViews.QR_ODG, name='qr_odg'),
    # path('qr_adms', QRViews.QR_ADMS, name='qr_adms'),
    # path('qrcode_all', QRViews.QRCode_all, name='qrcode_all'),
# Area Centers
    # path('qr_area1', QRViews.QR_Area1, name='qr_area1'),
    # path('qr_area2', QRViews.QR_Area2, name='qr_area2'),
    # path('qr_area3', QRViews.QR_Area3, name='qr_area3'),
    # path('qr_area4', QRViews.QR_Area4, name='qr_area4'),
    # path('qr_area5', QRViews.QR_Area5, name='qr_area5'),
    # path('qr_area6', QRViews.QR_Area6, name='qr_area6'),
    # path('qr_area7', QRViews.QR_Area7, name='qr_area7'),
    # path('qr_area8', QRViews.QR_Area8, name='qr_area8'),
    # path('qr_area9', QRViews.QR_Area9, name='qr_area9'),
    # path('qr_area10', QRViews.QR_Area10, name='qr_area10'),
    # path('qr_area11', QRViews.QR_Area11, name='qr_area11'),
    # path('qr_area12', QRViews.QR_Area12, name='qr_area12'),
# Show QR Code
    # path('caapid/show/<str:id>', QRViews.QR_Show, name='qr_show'),
# Create QR Code
    # path('qr_code/<int:id>', QRViews.AddQR, name='qr_code'),

# View PDF
    # path('page1_pdf_view/', PrintViews.ViewPDFPage1.as_view(), name="aansoo_view"),

    # Media Url Pattern    
    re_path(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], views.protected_serve, {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
