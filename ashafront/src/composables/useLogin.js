export function authorize(requestHandler,token){
    console.log('authorizing')
    this.$store.commit('setToken', token)
    requestHandler.defaults.headers.common["Authorization"] = "Token " + token
}
