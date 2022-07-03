<template>
{{cart}}
</template>

<script>
    export default {
        name: 'CartItem',
        data (){
            return {
                cartquantity : 0
            }
        },
        props : {
            cart: {
                type: Object,
                default: {},
            },
            quantity: {
                type: Number,
                default: 0,
            },
        },
        mounted(){
            this.cartquantity = cart.quantity
            console.log('this.cartquantity :>> ', this.cartquantity);
        }
    }
</script>
