from django.shortcuts import render

from .models import Product, BlogPost, Testimonial, TeamMember, Service, ContactInfo



# Create your views here.

def home(request):
    products = Product.objects.all()[:3]
    blog_posts = BlogPost.objects.all()[:3]  # Retrieve the latest 3 blog posts
    testimonials = Testimonial.objects.all()

    return render(request, 'index.html', {'navbar': 'home', 'products': products,'blog_posts': blog_posts, 'testimonials': testimonials} )



def shop(request):
    # Retrieve all products
    products = Product.objects.all()
    return render(request,'shop.html', {'navbar': 'shop', 'products': products})

def about(request):
    # Retrieve all team members
    team_members = TeamMember.objects.all()
    return render(request, 'about.html', {'navbar': 'about', 'team_members': team_members})

def services(request):
    # Retrieve all services
    services = Service.objects.all()
    return render(request, 'services.html', {'navbar': 'services', 'services': services})

def blog(request):
    blog_posts = BlogPost.objects.all()
    return render(request,'blog.html', {'navbar': 'blog', 'blog_posts': blog_posts})

def contact(request):
    contact_info = ContactInfo.objects.first()  # Assuming you have only one contact info entry
    return render(request,'contact.html', {'navbar': 'contact', 'contact_info': contact_info})

def cart(request):
    return render(request,'cart.html', {'navbar': 'cart'})

def checkout(request):
    # Replace this with your actual logic to retrieve product data for the order
    products_in_cart = Product.objects.filter(in_cart=True)

    # Calculate the total order amount
    total_amount = sum(product.price for product in products_in_cart)

    context = {
        'products_in_cart': products_in_cart,
        'total_amount': total_amount,
    }

    return render(request,'checkout.html', {'navbar': 'checkout'}, context)

def thankyou(request):
    return render(request,'thankyou.html', {'navbar': 'thankyou'})