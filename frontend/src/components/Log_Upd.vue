<template>
  <div>
		<fieldset>
			<h4>Update Tracker Details</h4>
			<form action="/:trackid/:logid/update" method="post">
			<!-- tracker name -->
				<label for="trak_name">Enter New Tracker Name:</label><br>
					<input type="text" id="trakname" name="trakname" value="{{ tracker.trk_name }}"><br><br>

			<!-- tracker description -->
				<label for="trak_desc">Enter New Tracker Description:</label><br>
					<input type="text" id="trakdesc" name="trakdesc" value="{{ tracker.description }}"><br><br>

      <!-- tracker type -->
      <label for="trak_type">Enter New Tracker Type:</label><br>
      <select id="trak_type" name="trak_type">
      <span v-for="x in track_type">
        <option value=":tracktypeid" v-if="tracker.trk_type==x.traktypeid" selected="selected" >{{ x.trak_type }}</option>
      </span>
    </select>
    <br><br>
    <label for="settings">If Multiple-Choice Tracker, Enter values separated by commas(,)</label><br>
    <textarea name="settings" rows="2" cols="30"></textarea><br>
			<br>

			<br>
				<input class="btn" type="submit" value="Update"><br><br>
			</form>

			<br><a href="/dashboard"> Back to Dashboard</a>
		</fieldset>
	</div>
</template>

<script>
export default {
  name: 'Log_Upd',
};
</script>

<style>
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
a:link {
color: white;
}
a:visited {
color: white;
}
a:hover {
color: #ffbbb1;
}
a:active {
color: white;
}
  </style>
