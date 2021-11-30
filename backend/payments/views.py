
from django.conf import settings
from rest_framework.views import APIView
import stripe
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

# This is a sample test API key. Sign in to see examples pre-filled with your key.
stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeCheckoutView(APIView):
    def post(self, request):
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                        'price': 'price_1K1We9KYN0O2KPac7alcd5RW',
                        'quantity': 1,
                    },
                ],
                payment_method_types=['card',],
                mode='payment',
                success_url=settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.SITE_URL + '/?canceled=true',
            )

            return redirect(checkout_session.url)
        except:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        

