from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem
from django.shortcuts import render, redirect
from django.http import JsonResponse
import stripe
import json
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,"index.html",)

def productDetails(request):
    return render(request, 'productDetails.html', )


def product(request):
    return render(request,"product.html")

def appl(request):
    return render(request,"appl.html")
def appl_det(request):
    return render(request,"appl_det.html")

def beauty(request):
    return render(request,"beauty.html")
def beauty_det(request):
    return render(request,"beauty_det.html")

def cam(request):
    return render(request,"cam.html")
def cam_details(request):
    return render(request,"cam_details.html")

def fru(request):
    return render(request,"fru.html")
def fru_det(request):
    return render(request,"fru_det.html")

def fur(request):
    return render(request,"fur.html")
def fur_det(request):
    return render(request,"fur_det.html")

def gro(request):
    return render(request,"gro.html")
def gro_det(request):
    return render(request,"gro_det.html")

def headset(request):
    return render(request,"headset.html")
def headset_det(request):
    return render(request,"headset_det.html")

def jew(request):
    return render(request,"jew.html")
def jew_det(request):
    return render(request,"jew_det.html")

def lap(request):
    return render(request,"lap.html")
def lap_det(request):
    return render(request,"lap_det.html")

def mob_product(request):
    return render(request,"mob_product.html")
def mob_product_det(request):
    return render(request,"mob_product_det.html")

def shoe(request):
    return render(request,"shoe.html")
def shoe_det(request):
    return render(request,"shoe_det.html")

def sta(request):
    return render(request,"sta.html")
def sta_det(request):
    return render(request,"sta_det.html")

def top(request):
    return render(request,"top.html")
def top_det(request):
    return render(request,"top_det.html")

def tshirt(request):
    return render(request,"tshirt.html")
def tshirt_det(request):
    return render(request,"tshirt_det.html")

def veg(request):
    return render(request,"veg.html")
def veg_det(request):
    return render(request,"veg_det.html")

def watch(request):
    return render(request,"watch.html")
def watch_det(request):
    return render(request,"watch_det.html")


# accounts/views.py


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now sign in.')
            return redirect('sign_in')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('index')  # Redirect to home page or dashboard
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})

# payment


# Initialize Stripe API with secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

def payment(request, product_name, product_price):
    context = {
        'product_name': product_name,
        'product_price': product_price,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'payment.html', context)

def create_checkout_session(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            product_name = data.get('product_name')
            product_price = data.get('product_price')  # Price in dollars

            # Convert price to cents (Stripe expects this)
            product_price_in_cents = int(product_price * 100)

            # Create the checkout session
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {'name': product_name},
                        'unit_amount': product_price_in_cents,
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/') + '?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=request.build_absolute_uri('/cancel/'),
            )

            # Return the session ID to redirect to the Stripe checkout
            return JsonResponse({'id': session.id})

        except Exception as e:
            # Log the error (optional)
            print(f"Error creating Stripe session: {e}")
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

def success(request):
    try:
        session_id = request.GET.get('session_id')
        if not session_id:
            return JsonResponse({'error': 'Session ID missing'}, status=400)

        session = stripe.checkout.Session.retrieve(session_id)
        customer_email = session.customer_details.email

        # Send email to the customer
        send_mail(
            'Payment Successful',
            f'Thank you for your purchase! Your payment for ${session.amount_total / 100:.2f} USD was successful.',
            'from@example.com',
            [customer_email],
            fail_silently=False,
        )

        return render(request, 'success.html', {'session': session})

    except Exception as e:
        # Log the error (optional)
        print(f"Error in success view: {e}")
        return JsonResponse({'error': str(e)}, status=500)

def cancel(request):
    return render(request, 'cancel.html')


def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")

# add to cart


def add_to_cart(request, product_name, product_price):
    product, created = Product.objects.get_or_create(name=product_name, price=product_price, discount=0)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

def cart_detail(request):
    cart_items = CartItem.objects.all()
    return render(request, 'cart_detail.html', {'cart_items': cart_items})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart_detail')
