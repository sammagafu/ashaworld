<template>
    <div class="page-content">
        <div class="container mt-10 mb-10">
            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-lg-6 offset-lg-3">
                    <h2 class="title title-center mb-4" style="margin-bottom: 1.9rem;">Hello, Register as Vendor</h2>
                    <form>
                        <!-- Email input -->

                        <div class="form-outline mb-4">
                            <input type="text" class="form-control" v-model="businessname" />
                            <label class="form-label">Compnay Name</label>
                        </div>

                        <div class="form-outline mb-4">
                            <select class="form-control" aria-label="Default select example" v-model="relationship">
                                <option value="Junior Employee">Junior Employee</option>
                                <option value="Senior Employee">Senior Employee</option>
                                <option value="Approved Representative">Approved Representative</option>
                                <option value="Owner">Owner</option>
                            </select>
                            <label class="form-label">Relation To Business</label>
                        </div>

                        <div class="form-outline mb-4">
                            <select class="form-control" aria-label="Default select example" v-model="accounttype">
                                <option value="Manufacture">Manufacture</option>
                                <option value="Reseller">Reseller</option>
                            </select>
                            <label class="form-label">Who are you?</label>
                        </div>

                        <div class="form-outline mb-4">
                            <input type="text" class="form-control" v-model="city" />
                            <label class="form-label">City</label>
                        </div>

                        <div class="form-outline mb-4">
                            <input type="text" class="form-control" v-model="country" />
                            <label class="form-label">Country</label>
                        </div>

                        <div class="form-outline mb-4">
                            <input type="phone" class="form-control" v-model="phone_number"
                                placeholder="+255 XXX XXX XXX" />
                            <label class="form-label">Bussiness Phone Number</label>
                        </div>

                        <div class="form-outline mb-4">
                            <textarea name="address" class="form-control" v-model="address"></textarea>
                            <label class="form-label">Bussiness Address</label>
                        </div>

                        <div class="form-outline mb-4">
                            <select class="form-control" aria-label="Default select example" v-model="status">
                                <option value="Registered">Registered</option>
                                <option value="Not Registered">Not Registered</option>
                            </select>
                            <label class="form-label">Business Status</label>
                        </div>

                        <div v-if="status == 'Registered' ">
                            <div class="form-outline mb-4">
                            <div class="form-group">
                                <input type="file" class="form-control" name="businessLincese">
                                <label class="form-label">Bussiness Lincence</label>
                            </div>
                        </div>

                         <div class="form-outline mb-4">
                            <div class="form-group">
                                <input type="file" class="form-control" name="tin">
                                <label class="form-label">Business Tax Identification Number Document (TIN)</label>
                            </div>
                        </div>
                        </div>

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

<script>
    export default {
        name:"VendorSignUp",
        data(){
            return{
                businessname : '',
                relationship : '',
                accounttype : '',
                city : '',
                country : '',
                phone_number : '',
                address : '',
                status : '',
                tin : '',
                businessLincese:''
            }
        },
    }
</script>

<style>

</style>