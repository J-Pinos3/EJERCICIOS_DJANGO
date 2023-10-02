import { useEffect, useState } from 'react'
import {useForm} from 'react-hook-form'
import {createTask, deleteTask, updateTask, getTask} from '../api/tasks.api'
import {useNavigate, useParams} from 'react-router-dom'
import { toast } from 'react-hot-toast'

export function TasksFormPage(){

    const{ register, handleSubmit, formState:{
        errors
    }, setValue } = useForm()

    const navigate = useNavigate()
    const params = useParams()
    console.log(params)


    const onSubmit = handleSubmit( async data =>{

        if(params.id){//si existe el id actualico
            console.log('actualizando')
            await updateTask(params.id, data)
            toast.success('Tarea Actualizada',{
                position:'bottom-right',
                style:{
                    background: '#101010',
                    color: '#fff'
                }
            })
            
        }else{//si no hay id, estoy creando
            const res = await createTask(data)//envía una petición post al back
            console.log(res)
            toast.success('Tarea creada',{
                position:'bottom-right',
                style:{
                    background: '#101010',
                    color: '#fff'
                }
            })
        }
        navigate('/tasks')
    })

    useEffect(()=>{
        
        async function loadTask(){
            if(params.id){
                console.log('obteniendo datos')
                const {data} = await getTask(params.id)
                console.log(data)
                setValue('title', data.title)
                setValue('description', data.description)
            }
        }
        loadTask()
    },[])

    return(
        <div className='max-w-xl mx-auto'>
            
            <form onSubmit={onSubmit}>

                <input type="text" placeholder="Title"
                    {...register('title', {required: true})}
                    className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'
                />
                {errors.title && <span>Field Required</span> }


                <textarea rows="3" placeholder="Description"
                    {...register('description', {required: true})}
                    className='bg-zinc-700 p-3 rounded-lg block w-full mb-3'
                ></textarea>
                {errors.description && <span>Field Required</span> }

                <button className='bg-indigo-500 p-3 rounded-lg block w-full mt-3'>Save</button>
            </form>

            { params.id && <button onClick={ async ()=>{ 
                const accepted = window.confirm('Are you sure?')
                
                if(accepted){
                    await deleteTask(params.id)
                    toast.success('Tarea Eliminada',{
                        position:'bottom-right',
                        style:{
                            background: '#101010',
                            color: '#fff'
                        }
                    })
                    navigate('/tasks')
                }
                

            }}>Delete</button>}

        </div>
    ) 
}