from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    #print("tipo de peticion: {}".format(request.method))
    #instanciar el formulario
    contact_form = ContactForm()
    
    if (request.method == "POST"):
        #si el metodo es post guardo los datos del formulario
        contact_form = ContactForm(data=request.POST)
        if (contact_form.is_valid()):
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #ENVIAR EL CORREO Y REDIRECCIONAR
            email = EmailMessage(
                "La Caffetiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,content),
                "no-contestar@ibox.mailtrap.io",
                ["pooljpv84@gmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
                #todo ha ido bien, redireccionamos a ok
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no ha ido bien, redireccionamos a fail
                return redirect(reverse('contact')+"?fail")
            

    return render(request,"contact/contact.html", {'form': contact_form})

