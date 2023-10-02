import {useForm} from 'react-hook-form'

export function TasksFormPage(){

    const{ register, handleSubmit, formState:{
        errors
    } } = useForm()

    const onSubmit = handleSubmit(date =>{
        console.log(date)
    })

    return(
        <div>
            
            <form onSubmit={onSubmit}>

                <input type="text" placeholder="Title"
                    {...register('title', {required: true})}
                />
                {errors.title && <span>Field Required</span> }


                <textarea rows="3" placeholder="Description"
                    {...register('description', {required: true})}
                ></textarea>
                {errors.description && <span>Field Required</span> }

                <button>Save</button>
            </form>

        </div>
    ) 
}