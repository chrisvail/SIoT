<script>
    import TaskCard from "../components/cards/task_card.svelte";


    let tasks = {
        todo:[
            {
                title: "Add 10ml of Nutrient A",
                body: "The EC is getting a bit low, add some nutrient to keep those plants growing",
            },
            {
                title: "Check on unit 2",
                body: "We haven't seen readings from unit 2 for a while, check its plugged in",
            },
            {
                title: "Add some pH up",
                body: "The pH is predicted to drop soon, add some pH booster to help keep it steady",
            }
        ],
        claimed:[
            {
                title: "Harvest your tomatoes",
                body: "We think those tomatoes are ready to harvest. Go get them!",
                person:{
                    name:"Jack Pollington",
                    src: "static/favicon.png"
                }
            },
            {
                title: "Harvest your tomatoes",
                body: "We think those tomatoes are ready to harvest. Go get them!",
                person:{
                    name:"Karen McLeod",
                    src: "static/favicon.png"
                }
            }
        ],
        done:[
            {
                title: "Set up the system",
                body: "Time to get started! Head to our quickstart guide now to get everything up and running",
                person:{
                    name:"Chris Vail",
                    src: "static/favicon.png"
                }
            },
        ]
    }

    const claim = (e, unit) => {
        let ind = tasks.todo.indexOf(unit)
        tasks.todo.splice(ind, 1)
        unit.person = {name: "Chris Vail"}
        console.log(unit)
        tasks.claimed.push(unit)
        tasks = tasks

    }

    const complete = (e, unit) => {
        let ind = tasks.claimed.indexOf(unit)
        tasks.claimed.splice(ind, 1)
        tasks.done.push(unit)
        tasks.claimed = tasks.claimed
        tasks.done = tasks.done
        tasks = tasks

    }

    const hide = (e, unit) => {
        let ind = tasks.done.indexOf(unit)
        tasks.done.splice(ind, 1)
        tasks.done = tasks.done
    }

</script>


<main class="grid">
    <h1>Tasks</h1>
    <div class="column start">
        <h3>To Do</h3>
        {#each tasks.todo as task}
            <TaskCard {...task} unit={task} buttonText="Claim" buttonClick={claim}/>
        {/each}
    </div>
    <div class="column">
        <h3>Claimed</h3>
        {#each tasks.claimed as task}
            <TaskCard {...task} unit={task} buttonText="Completed" buttonClick={complete}/>
        {/each}
    </div>
    <div class="column">
        <h3>Done</h3>
        {#each tasks.done as task}
            <TaskCard {...task} unit={task} buttonText="Hide"buttonClick={hide} />
        {/each}
    </div>


</main>


<style>

    .column {
        grid-column: span 4;
    }

    h3 {
        font-size: 2em;
    }

    .start {
        grid-column: content-start / span 4;
    }

</style>