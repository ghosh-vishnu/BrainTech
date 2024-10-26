from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Certificate
from .forms import CertificateForm

# Home Page
def home(request):
    return render(request, 'index.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

# Career Page
def career(request):
    return render(request, 'carrer.html')  # Corrected spelling

# Service Page
def service(request):
    return render(request, 'service.html')

# Software Developer Intern Page
def software_intern(request):
    return render(request, 'software-developer-intern.html')

# Thanks Page
def thanks(request):
    return render(request, 'thanks.html')

# Verify Page
def verify(request):
    return render(request, 'verify.html')

# Web Developer Intern Page
def web_intern(request):
    return render(request, 'web-developer-intern.html')

# Certificate Verification Logic
def verify_certificate(request):
    if request.method == "POST":
        certificate_number = request.POST.get('certificate_number')
        try:
            certificate = Certificate.objects.get(certificate_number=certificate_number)
            # Check if the certificate file is uploaded
            if certificate.certificate_file:
                return render(request, 'verify.html', {'certificate': certificate})
            else:
                message = "Your certificate has not been generated. Please wait a few days."
                return render(request, 'verify.html', {'message': message})
        except Certificate.DoesNotExist:
            error = "No record found"
            return render(request, 'verify.html', {'error': error})

    return redirect('verify')  # Redirect on non-POST requests

# Certificate Download Logic
def download_certificate(request, certificate_number):
    # Fetch the certificate from the database based on the certificate number
    certificate = get_object_or_404(Certificate, certificate_number=certificate_number)

    # Check if the certificate file is available
    if not certificate.certificate_file:
        # Display a message if the certificate file is not uploaded
        message = "Currently, your certificate has not been generated. Please wait a few days."
        return render(request, 'verify.html', {'message': message})

    # Use the correct field name for the certificate file
    filepath = certificate.certificate_file.path  # Path to the certificate file

    try:
        with open(filepath, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{certificate.certificate_number}.pdf"'  # Dynamic filename
            return response
    except FileNotFoundError:
        raise Http404("Certificate not found")

# Upload Certificate Logic
def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save(commit=False)  # Save the form without committing to the database yet
            # Save the certificate file if it exists, else save without it
            if request.FILES.get('certificate_file'):
                certificate.certificate_file = request.FILES['certificate_file']
            certificate.save()  # Save the data to the database
            return redirect('success')  # Success page redirect
    else:
        form = CertificateForm()
    
    return render(request, 'upload_certificate.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')
