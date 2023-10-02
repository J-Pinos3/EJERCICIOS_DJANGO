import axios from 'axios'

const taskAPI = axios.create({
    baseURL: 'http://127.0.0.1:8000/tasks/api/v1/tasks/'
})

export const getAllTasks = ()=>{
    //return axios.get('http://127.0.0.1:8000/tasks/api/v1/tasks/') EQUIVALENTES
    return taskAPI.get('/')
}

export const getTask = (id) => taskAPI.get(`/${id}/`)

// MÁS RESUMIDO >:)
export const createTask =(task)=> taskAPI.post('/', task)

export const deleteTask =(id)=> taskAPI.delete(`/${id}`)

export const updateTask =(id, task)=> taskAPI.put(`/${id}/`, task)

