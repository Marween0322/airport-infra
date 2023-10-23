from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import filesizeformat
from django.conf import settings

from .models import Personal,Payroll, Children, Education, Eligibility, Experience, Voluntary, Learning, Otherinfo, Refferences, Other_skills, Other_recognitions, Other_membership, Vaccine,Training,Leave, SPFLeave, SalaryGrade, Position, Signatory, Post, NotifyTraining, Bonuses, Qrcode

class PersonalInfoForm(forms.ModelForm):

      class Meta:
            model = Personal
            fields = "__all__"
            labels = {
            'ext_name': _('Extension Name (JR., SR)'),
            'birth_date': _('Date of Birth'),
            'birth_place': _('Place of Birth'),
            'citizen_detail': _('If holder of  dual citizenship, please indicate the details.'),
            'gsis': _('GSIS ID No.'),
            'pagibig': _('PAG-IBIG ID No.'),
            'philhealth': _('Philhealth No.'),
            'sss': _('SSS No.'),
            'res_numstreet': _('Street number/name/building/purok'),
            'res_brgy': _('Barangay'),
            'res_city': _('City.'),
            'res_province': _('Province.'),
            'res_zip': _('ZIP Code.'),
            'perma_numstreet': _('Street number/name/building/purok'),
            'perma_brgy': _('Barangay'),
            'perma_city': _('City'),
            'perma_province': _('Province'),
            'perma_zip': _('ZIP Code'),
            'emp_number': _('CAAP Employee Number'),
            'tin': _('TIN'),
            'spouse_surname': _('Surname'),
            'spouse_name': _('First Name'),
            'spouse_middle': _('Middle Name'),
            'spouse_ext': _('Extension Name'),
            'spouse_occupation': _('Occupation'),
            'phone': _('Phone Number'),
            'emb_biz': _('Employer Name'),
            'emb_biz_add': _('Employer Address'),
            'dad_surname': _('Surname'),
            'dad_name': _('First Name'),
            'dad_middle': _('Middle Name'),
            'dad_ext': _('Extension Name'),
            'mom_surname': _('Surname'),
            'mom_name': _('First Name'),
            'mom_middle': _('Middle Name'),}

def clean_content(self):
          content = self.cleaned_data['content']
          content_type = content.content_type.split('/')[0]
          if content_type in settings.CONTENT_TYPES:
              if content._size > settings.MAX_UPLOAD_SIZE:
                  raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
          else:
              raise forms.ValidationError(_('File type is not supported'))
          return content


class ChildrenForm(forms.ModelForm):

      class Meta:
            model = Children
            fields = "__all__"
            labels = {
            'name': _('Full Name'),
            'birth_date': _('Date of Birth'),
        }


class UserForm(forms.ModelForm):

      class Meta:
            model = User
            fields = "__all__"     


class EducationForm(forms.ModelForm):

      class Meta:
            model = Education
            fields = "__all__"
            labels = {
            'school': _('Name of School'),
            'grad_year': _('Year Graduated'),
            'units': _('Highest Level/Units Earned'),
            'course': _('Basic Education/Degree/Course (Write in full)'),
            'date_from': _('Period of Attendance From (ex. 1998)'),
            'date_to': _('Period of Attendance To (ex. 2001)'),
            'honors': _('Scholarship/Academic Honors Recieve'),
        }

class EligibilityForm(forms.ModelForm):

      class Meta:
            model = Eligibility
            fields = "__all__"
            labels = {
            'place': _('Place of Exam/Conferment'),
            'lic_number': _('License Number (If Applicable)'),
        }

class ExperienceForm(forms.ModelForm):

      class Meta:
            model = Experience
            fields = "__all__"
            labels = {
            'position': _('Position Title'),
            'department': _('Department/Agency/Office/Company'),
            'salary': _('Monthly Salary'),
            'increment': _('Salary Grade & Step Increment(Format "00-0")'),
            'appointment': _('Status of Appointment'),
            'govt_service': _('Goverment Service (Yes / No)'),
            }

class VoluntaryForm(forms.ModelForm):

      class Meta:
            model = Voluntary
            fields = "__all__"
            labels = {
            'name': _('Name & Address of Organization'),
            'hours': _('Number of Hours'),
            'position': _('Position / Nature of Work'),
            }

class LearningForm(forms.ModelForm):

      class Meta:
            model = Learning
            fields = "__all__"
            labels = {
            'title': _('Title of Learning and Development Interventions/Training Programs'),
            'venue': _('Venue'),
            'learning_type': _('Type of Learning and Development'),
            'training_hours': _('Number of Hours'),
            'fee': _('Course Fee'),
            'conducted_by': _('Conducted/ Sponsored By'),
            }

class OtherinfoForm(forms.ModelForm):

      class Meta:
            model = Otherinfo
            fields = "__all__"
            labels = {
            'related_detail_3': _(' If YES, give details:'),
            'related_detail_4': _(' If YES, give details:'),
            'admin_offense_detail': _(' If YES, give details:'),
            'crime_detail': _(' If YES, give details ssStatus of Case/s:'),
            'crime_date': _('  Date Filed '),
            'convic_detail': _(' If YES, give details:'),
            'seperated_detail': _(' If YES, give details:'),
            'candidate_detail': _(' If YES, give details:'),
            'resigned_detail': _(' If YES, give details:'),
            'immigrant_detail': _(' If YES, give details (Country):'),
            'indigenous_detail': _(' If YES, give details:'),
            'disability_detail': _(' If YES, specify ID number and upload certificate:'),
            'soloparent_detail': _(' If YES, specify ID number and upload certificate:'),
        }

class RefferencesForm(forms.ModelForm):

      class Meta:
            model = Refferences
            fields = "__all__"
            labels = {
            'name': _('Full Name'),
            'phone': _('Contact'),
            }

class Other_skillsForm(forms.ModelForm):

      class Meta: 
            model = Other_skills
            fields = "__all__"
            labels = {
            'skills': _('Special Skills and Hobbies'),
            }

class Other_recognitionsForm(forms.ModelForm):  

      class Meta:
            model = Other_recognitions
            fields = "__all__"
            labels = {
            'recognition': _('NON-ACADEMIC DISTINCTIONS / RECOGNITION (Write in full)'),
            }

class Other_membershipForm(forms.ModelForm):

      class Meta:
            model = Other_membership
            fields = "__all__"
            labels = {
            'member_org': _('MEMBERSHIP IN ASSOCIATION/ORGANIZATION (Write in full)'),
            }

class VaccineForm(forms.ModelForm):

      class Meta: 
            model = Vaccine
            fields = "__all__"
            labels = {
            'name1': _('Vaccine Manufacturer'),
            'place1': _('Place of Vaccine'),
            'file1': _('Upload first dose vaccine Image. (JPEG, JPG)'),
            'name2': _('Vaccine Manufacturer'),
            'place2': _('Place of Vaccine'),
            'file2': _('Upload secon dose vaccine Image. (JPEG, JPG)'),
            'name3': _('Vaccine Manufacturer'),
            'place3': _('Place of Vaccine'),
            'file3': _('Upload booster vaccine Image. (JPEG, JPG)'),
            'name4': _('Vaccine Manufacturer'),
            'place4': _('Place of Vaccine'),
            'file4': _('Upload booster vaccine Image. (JPEG, JPG)'),
        }

class CreateTrainingForm(forms.ModelForm):

      class Meta:
            model = Training
            fields = "__all__"

class PayrollForm(forms.ModelForm):

      class Meta:
            model = Payroll
            fields = "__all__"

class LeaveForm(forms.ModelForm):

      class Meta:
            model = Leave
            fields = "__all__"

class SPFLeaveForm(forms.ModelForm):

      class Meta:
            model = SPFLeave
            fields = "__all__"

class SalaryGradeForm(forms.ModelForm):

      class Meta:
            model = SalaryGrade
            fields = "__all__"

class PositionForm(forms.ModelForm):

      class Meta:
            model = Position
            fields = "__all__"

class SignatoryForm(forms.ModelForm):

      class Meta:
            model = Signatory
            fields = "__all__"

class PostForm(forms.ModelForm):

      class Meta:
            model = Post
            fields = "__all__"

      def clean_content(self):
          content = self.cleaned_data['content']
          content_type = content.content_type.split('/')[0]
          if content_type in settings.CONTENT_TYPES:
              if content._size > settings.MAX_UPLOAD_SIZE:
                  raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(content._size)))
          else:
              raise forms.ValidationError(_('File type is not supported'))
          return content


class NotifyTrainingForm(forms.ModelForm):
      
      class Meta:
            model = NotifyTraining
            fields = "__all__"   

class BonusForm(forms.ModelForm):
      
      class Meta:
            model = Bonuses
            fields = "__all__"      

class QrcodeForm(forms.ModelForm):

      class Meta:
            model = Qrcode
            fields = "__all__"  