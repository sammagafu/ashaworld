<template>
    <div class="page-content">
        <div class="container mt-10 mb-10">
            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-lg-6 offset-lg-3">
                <h2 class="title title-center mb-4" style="margin-bottom: 1.9rem;">Hello</h2>
                <p class="text-center">Register to Asha or <router-link :to="{name:'login'}">Login to your account
                    </router-link>
                </p>
                <form>
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
                        <input type="text" class="form-control" v-model="username"/>
                        <label class="form-label">Username</label>
                    </div>

                    <div class="form-outline mb-4">
                        <input type="email" class="form-control" v-model="email"/>
                        <label class="form-label">E-Mail</label>
                    </div>

                    <!-- Password input -->
                    <div class="form-outline mb-4">
                        <input type="password" class="form-control" v-model="password" />
                        <label class="form-label" for="loginPassword">Password</label>
                    </div>

                    <p>Your personal data will be used to support your experience 
                    throughout this website, to manage access to your account, 
                    and for other purposes described in our <a href="#" class="text-primary">privacy policy</a>.</p>

                    <!-- Submit button -->
                    <div class="row mb-4">
                        <div class="col-md-12 d-flex justify-content-center">
                           <input type="submit" value="Register" class="btn btn-block btn-primary">
                        </div>
                    </div>

                    <!-- Register buttons -->
                    <div class="text-center">
                        <p>Not a member? <a href="#!">Register</a></p>
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

import axios from 'axios'
export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            email: '',
            password: '',
            errors: []
        }
    },
    methods: {
        submitForm() {
            this.errors = []
            if (this.username === '') {
                this.errors.push('The username is missing')
            }
            if (this.password === '') {
                this.errors.push('The password is too short')
            }
            if (!this.errors.length) {
                const formData = {
                    email: this.email,
                    password: this.password
                }
                axios
                    .post("/api/v1/users/", formData)
                    .then(response => {
                        this.$router.push('/log-in')
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                            console.log(JSON.stringify(error.response.data))
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again')
                            
                            console.log(JSON.stringify(error))
                        }
                    })
            }
        }
    }
}
</script>