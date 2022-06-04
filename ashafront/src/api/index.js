import axios from "axios";
import categoryAPI from "./categories.api";

const axiosInstance = axios.create({
    baseURL:"/api/v1",
    // headers:{
    //     "Content-Type": 
    // }
})

const categoryService = categoryAPI({ axios: axiosInstance })

export {
   categoryService
}