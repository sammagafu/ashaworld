
const categoryAPI = function({ axios }){

    return {
        fetchCategories:async function(){
            const { data } = axios.get("/category/")
            return data
        }

    }
}

export default categoryAPI