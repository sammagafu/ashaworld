<template>
    <div class="page-content">
        <div class="container mt-10 mb-10">
            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-lg-6 offset-lg-3">
                <h2 class="title title-center mb-4" style="margin-bottom: 1.9rem;">Hello</h2>
                <p class="text-center">Sign in to Asha or <router-link :to="{name:'signup'}">create an account
                    </router-link>
                </p>
                <form @submit.prevent="loginUser">
                    <div class="text-center mb-3">
                        <p>Sign in with:</p>
                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-facebook-f"></i>
                        </button>

                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-google"></i>
                        </button>

                        <button type="button" class="btn btn-link btn-floating mx-1">
                            <i class="fab fa-apple"></i>
                        </button>
                    </div>

                    <p class="text-center">or:</p>

                    <!-- Email input -->
                    <div class="form-outline mb-4">
                        <input type="email" class="form-control" v-model="email"/>
                        <label class="form-label">Email</label>
                    </div>

                    <!-- Password input -->
                    <div class="form-outline mb-4">
                        <input type="password" id="loginPassword" class="form-control" v-model="password"/>
                        <label class="form-label" for="loginPassword">Password</label>
                    </div>

                    <!-- 2 column grid layout -->
                    <div class="row mb-4">
                        <div class="col-md-6 d-flex justify-content-center">
                            <!-- Checkbox -->
                            <div class="form-check mb-3 mb-md-0">
                                <input class="form-check-input" type="checkbox" value="" id="loginCheck" checked />
                                <label class="form-check-label" for="loginCheck"> Remember me </label>
                            </div>
                        </div>

                        <div class="col-md-6 d-flex justify-content-center">
                            <!-- Simple link -->
                            <a href="#!">Forgot password?</a>
                        </div>
                    </div>
                    <div class="row mb-4">
                        <div class="col-md-6 d-flex justify-content-center">
                           <input type="submit" value="Sign in" class="btn btn-block btn-primary">
                        </div>
                    </div>

                    <!-- Register buttons -->
                    <div class="text-center">
                        <p>Not a member?<router-link :to="{name:'signup'}">Register</router-link></p>
                        <!-- <p>Not a member? <a href="#!">Register</a></p> -->
                    </div>
                </form>
            </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
button{
    margin: 10px 24px; 
}
.fab{
    font-size: 25;
}
</style>

<script>
import axios from 'axios';

export default{
    name:'Login',
    data(){
        return{
            email : '',
            password : '',
            errors: [],
        }
    },
    mounted() {
        document.title = 'Log In | Asha'
    },
    methods:{
        async loginUser(){
            axios.defaults.headers.common["Authorization"] = ""
            localStorage.removeItem("token")

            const loginData = {
                email : this.email,
                password : this.password
            }
        await axios.post('token/login/',loginData)
            .then(response =>{
                const token = response.data.auth_token
                this.$store.commit('setToken', token)
                axios.defaults.headers.common["Authorization"] = "Token " + token
                localStorage.setItem("token", token)

                const toPath = this.$route.query.to || '/cart'
                this.$router.push(toPath)

                // console.log('response :>> ', response.data.auth_token);
            }).catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
        })
    
    }
    
    }

}
</script>