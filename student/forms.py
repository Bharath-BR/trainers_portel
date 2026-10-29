from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model=Student
        fields=['name','roll_no','marks','email','course','address']

        widgets={
            'name':forms.TextInput(
                attrs={
                    'placeholder':"Enter Student's Name"
                }
            ),

            'roll_no':forms.NumberInput(
                attrs={
                    'placeholder':"Enter Student's Roll Number"
                }
            ),

            'marks':forms.NumberInput(
                attrs={
                    'placeholder':"Enter Student's Marks"         
                }
            ),

            'email':forms.EmailInput(
                attrs= {
                    'placeholder':"Enter Student's Email"  
                }       
            ),

            'course':forms.TextInput(
                attrs={
                    'placeholder':"Enter Student's Course" 
                }
            ),

            'contact':forms.TextInput(
                attrs={
                    'placeholder':"Enter Student's Ph No"
                }
            ),

            'address':forms.Textarea(
                attrs={
                    'placeholder':"Enter Student's Address",
                    'rows':10,
                    'cols':50,
                }
            )
        }

    def clean_roll_no(self):
        roll_no=self.cleaned_data['roll_no']

        if roll_no < 0:
            raise forms.ValidationError('Roll Number cannot be negative')
        return roll_no

    def clean_marks(self):
        marks=self.cleaned_data['marks']

        if marks<0 or marks>100:
            raise forms.ValidationError('Marks must be in the range of 0 to 100')
        return marks
    
    def clean_contact(self):
        contact=self.cleaned_data['contact']

        if len(contact)!=10:
            raise forms.ValidationError('Contact must contain exactly 10 digits')
        
        return contact

    def create(self,user):
        # name=self.cleaned_data['name']
        # roll_no=self.cleaned_data['roll_no']
        # marks=self.cleaned_data['marks']
        # email=self.cleaned_data['email']
        # course=self.cleaned_data['course']
        # contact=self.cleaned_data['contact']
        # address=self.cleaned_data['address']
            
        # student=Student.objects.create(name=name, roll_no=roll_no, marks=marks,
        # email=email, course=course, contact=contact, address=address,trainer=user)

        student=Student.objects.create(trainer=user,**self.cleaned_data)
        return student

    def update(self,instance):
        instance.name=self.cleaned_data.get('name',instance.name)
        instance.roll_no=self.cleaned_data.get('roll_no',instance.roll_no)
        instance.marks=self.cleaned_data.get('marks',instance.marks)
        instance.email=self.cleaned_data.get('email',instance.email)
        instance.course=self.cleaned_data.get('course',instance.course)
        instance.contact=self.cleaned_data.get('contact',instance.contact)
        instance.address=self.cleaned_data.get('address',instance.address)

        instance.save()

        return instance
