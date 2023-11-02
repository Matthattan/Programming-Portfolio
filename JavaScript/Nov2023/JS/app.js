const app = Vue.createApp({
    // you can add data, templates and methods here
    data() {
        return {
            title: "Hitchhiker's guide to the galaxy",
            author: "Douglas Adams",
            age: 42,
            // condition to show or hide books
            showBooks: true
        }
    },
    // Function to change title on HTML
    methods: {
        changeTitle(title) {
            this.title =  title
        },
        // do the inverse of what the current state of showBooks is
        toggleShowBooks() {
            this.showBooks = !this.showBooks

        }
    }
})

app.mount('#app')