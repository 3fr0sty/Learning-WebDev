const { createApp } = Vue;

createApp({
    data() {
        return {
            username: null
        };
    },

    async mounted(){
        const response = await fetch("/whoami")
        const data = await response.json()
        this.username = data.logged_in_as;
    }
}).mount("#navbar")

createApp({
    data() {
        return {
            workoutList: ["Left day", "Neck and eyelids", "Glutes and right heel workout", "Mega rest day"],
            newWorkout: "",
            methods: {
                addWorkout() {
                    
                }
            }
        }
    }
}).mount(".content")