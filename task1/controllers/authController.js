const User=require("../models/User");
const bcrypt=require("bcryptjs");
const jwt=require("jsonwebtoken");

const signup=async (req,res)=>
{
    try
    {
        const { email, password }=req.body;
        const hashedPassword=await bcrypt.hash(password,10);

        const checkUser=await User.findOne({email});
        if(checkUser)
        {
            return res.status(400).json({error: "User already exists!"});
        }

        const user=await User.create({email,password: hashedPassword});
        res.json({message: "User created successfully!"});
    }
    catch(err)
    {
        console.log(err);
        res.status(500).json({error: "Error creating user!"});
    }
}

const login=async (req,res)=>
{
    try
    {
        const { email, password }=req.body;
        const user=await User.findOne({email});

        if(!user)
        {
            return res.status(400).json({error: "User not found!"});
        }

        const passwordMatch=await bcrypt.compare(password,user.password);
        if(!passwordMatch)
        {
            return res.status(401).json({error: "Invalid credentials!"});
        }

        const token=jwt.sign({userId: user._id},process.env.SECRET_KEY,{expiresIn: "1h"});
        res.json({token});
    }
    catch(err)
    {
        res.status(500).json({error: "Error logging in!"});
    }
}

module.exports={ login, signup };