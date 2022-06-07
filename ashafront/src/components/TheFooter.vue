<template>
    <div class="footer-newsletter bg-primary pt-6 pb-6">
        <div class="container">
            <div class="row justify-content-center align-items-center">
                <div class="col-xl-5 col-lg-6">
                    <div class="icon-box icon-box-side text-white">
                        <div class="icon-box-icon d-inline-flex">
                            <i class="w-icon-envelop3"></i>
                        </div>
                        <div class="icon-box-content">
                            <h4 class="icon-box-title text-white text-uppercase mb-0">Subscribe To Our
                                Newsletter</h4>
                            <p class="text-white">Get all the latest information on Events, Sales and Offers.
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-xl-7 col-lg-6 col-md-9 mt-4 mt-lg-0 ">
                    <form action="#" method="get" class="input-wrapper input-wrapper-inline input-wrapper-rounded">
                        <input type="email" class="form-control mr-2 bg-white" name="email" id="email"
                            placeholder="Your E-mail Address">
                        <button class="btn btn-dark btn-rounded" type="submit">Subscribe<i
                                class="w-icon-long-arrow-right"></i></button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="footer-bottom">

            <div class="footer-left">
                <p class="copyright">Copyright &copy; {{new Date().getFullYear()}} Asha. All Rights Reserved.</p>
            </div>
            <div class="footer-right">
                <span class="payment-label mr-lg-8">We're using safe payment for</span>
                <figure class="payment">
                    <img src="../assets/images/payment.png" alt="payment" width="159" height="25">
                </figure>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TheFooter"
    }
</script>