const express=require("express");
const app=express();

const dotenv=require("dotenv");

dotenv.config();

app.use(express.json());

const connectDB=require("./config/db");
connectDB();

const userRoutes=require("./routes/userRoutes");
app.use("",userRoutes);

const PORT=process.env.PORT || 5000;

app.listen(PORT,console.log(`Server listening on PORT:${PORT}`));