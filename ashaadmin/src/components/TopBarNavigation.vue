<template>
    <div class="navbar-menu">
        <div class="navbar-start">
            <a class="navbar-item">
                <img src="../assets/asha-logo-dark.svg" alt="">
                <!-- <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28" alt="Bulma"> -->
            </a>
        </div>

        <div class="navbar-end">
            <div class="navbar-item">
                <p class="control">
                    <a class="button is-primary"
                        href="https://github.com/jgthms/bulma/releases/download/0.9.4/bulma-0.9.4.zip">
                        <span class="icon">
                            <i class="fas fa-download"></i>
                        </span>
                        <span>Download</span>
                    </a>
                </p>
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        name: 'ToPBarNavigation'
    }
</script>

<style>
    .nav-header {
        background-color: black !important;
    }
</style>