const express = require("express")

const router = express.Router();

router.get("/", async (req, res) => {
    try {
        return res.send("Hello World!")
    } catch(error) {
        res.status(400).send({ error })
    }
})

module.exports = app => app.use("/", router) 