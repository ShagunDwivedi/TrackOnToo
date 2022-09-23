<template>
  <div>
    <fieldset>
<h4>Update Tracker Details</h4>
<!-- tracker name -->
<label for="trak_name">Enter New Tracker Name:</label><br>
<input type="text" id="trakname" name="trakname" v-model="trackname"><br><br>

<!-- tracker description -->
<label for="trak_desc">Enter New Tracker Description:</label><br>
<input type="text" id="trakdesc" name="trakdesc" v-model="desc" ><br><br>

<!-- tracker type -->
<label for="trak_type">Enter New Tracker Type:</label><br>
<select id="trak_type" name="trak_type" v-model="tracktype">
<option :value="1">Numeric</option>
<option :value="2">Boolean</option>
<option :value="3">Multiple Choice</option>
<option :value="4">Time Duration</option>
</select>
<br><br>
<span v-if="tracktype === '3' | tracktype === 'Multiple Choice'">
<label for="settings">Enter values separated by commas(,)</label><br>
<input type="text" id="settings" name="settings" v-model="settings"><br>
<br>
</span>
<button id="submit" name="submit" type="submit" class="btn" @click.prevent="submitted">
Update</button>
<br><br>

<br><a @click="pushDash"> Back to Dashboard</a>
</fieldset>
</div>
</template>

<script>
function json(response) {
  return response.json();
}
export default {
  name: 'Tracker_Upd',
  data() {
    return {
      trackname: '',
      desc: '',
      tracktype: '',
      settings: '',
      msg: '',
      trackid: localStorage.getItem('id'),
    };
  },
  mounted() {
    fetch(`http://127.0.0.1:5000/api/tracker/${this.trackid}`, {
      method: 'get',
      mode: 'cors',
      headers: {
        'Content-type': 'application/json',
        Authorization: localStorage.getItem('access_token'),
      },
    })
      .then(json)
      .then((data) => {
        if (data.id) {
          this.trackname = data.name;
          this.desc = data.description;
          this.tracktype = data.type;
          this.settings = data.settings;
        } else {
          this.msg = data.msg;
        }
      });
  },
  methods: {
    pushDash() {
      this.$router.push('/dashboard');
    },
    submitted() {
      fetch(`http://127.0.0.1:5000/api/tracker/${this.trackid}`, {
        method: 'patch',
        mode: 'cors',
        headers: {
          'Content-type': 'application/json',
          Authorization: localStorage.getItem('access_token'),
        },
        body: JSON.stringify({
          name: this.trackname,
          description: this.desc,
          type: this.tracktype,
          settings: this.settings,
        }),
      })
        .then(json)
        .then((data) => {
          if (data.msg === 'Success') {
            this.pushDash();
          } else {
            this.msg = data.msg;
          }
        });
    },
  },
};
</script>

<style scoped>
    body{
background-color: #ffbbb1;
background-attachment: fixed;
background-size: cover;
background-repeat: no-repeat;
background-position: center center;
margin-top: 0px;
margin-left: 0px;
margin-right: 0px;
}
.trkname{
  display: block;
  padding-inline-start: 40px;
  background-color: #653187;
  overflow: hidden;
  margin-top: 0px;
  color: white;
}
a:hover {
  color:#ffbbb1;
  cursor: pointer;
}
ul {
  list-style-type: none;
  margin: 5px;
  padding: 8px;
  background-color: #FFDAC1;
  overflow: hidden;
  color: black;
  width: 60%
}

li {
  float: left;
  display: block;
  border-right: 1px solid black;
}

li a{
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  cursor: pointer;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  color: white;
}
.btn{
  width: 10%;
  background-color: white;
  cursor: pointer;
  padding: 10px 8px;
  border: none;
  color: #653187;
  margin-left: 5px;
}
.btn:hover{
  background-color: #ffbbb1;
  color: #653187;
}
fieldset{
  display: block;
  background-color: #653187;
  width: 50%;
  margin-left: auto;
  margin-right: auto;
  text-align: center;
  border-style: none;
  color:white;
}
  </style>
