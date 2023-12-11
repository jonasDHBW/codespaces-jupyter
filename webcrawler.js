const superagent = require('superagent').agent();

const ytm = async () => {
    let dashboard = await superagent
    .post('https://auth0.openai.com/u/login/identifier?state=hKFo2SBMTmNwMkM1RDVyVnJkVXpOXzVGX2t6TkVlS1hleml5cqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEh1c25WOEk2WjNXTVptZ3VPdlRyZ3EyVUZZVEZBSlFXo2NpZNkgVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEc')
    .send({usernames: 'jonas', passwords })
}
