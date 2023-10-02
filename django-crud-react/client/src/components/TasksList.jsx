import { useEffect, useState } from 'react'
import { getAllTasks } from '../api/tasks.api'
import { TasksCard } from './TaskCard'

export function TasksList() {

    const [tasks, setTasks] = useState([])

    //use effect se usa cuando se entra en la página
    useEffect(() => {

        async function loadTasks() {
            const res = await getAllTasks()
            setTasks(res.data)
            console.log(res)
        }
        loadTasks()

    }, [])


    return( 
    <div className='grid grid-cols-3 gap-3'>

        {tasks.map( task =>(
            <TasksCard key={task.id} task={task}/>
        ))}

    </div>
    );
}