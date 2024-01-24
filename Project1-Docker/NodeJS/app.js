const express = require('express')
const app= express()

app.get('/',(req,res)=> res.send('hello World'))

// app.listen(3000,()=>console.log('server ready'))
const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server listening on port ${port}`));