<script type="text/javascript" src="/scripts/ace/ace.js"></script>
	
<h1> Edit plugin {{.name}} </h1>
<p>
	{{if .error}}
	Compilation errors: <br />
	{{.error}}
	{{end}}
</p>
<form action="/plugins/edit" method="POST" onsubmit="document.getElementById('contentT').value = ace.edit('content').getSession().getValue();">
	<input type="hidden" value="{{.name}}" name="oldname" />
	<textarea cols="100" rows="40" name="content" id="contentT">{{.content}}</textarea> <br />
	<div id="content" style="height: 550px; width: 900px;"></div> <br />
	Save: <input type="text" name="filename" value="{{.name}}" /><input type="submit" value="Submit" name="submit" /><input type="submit" value="Save and reload plugin" name="submit" />
</form>

<script type="text/javascript"> 
	var editor = ace.edit("content");
	var textarea = document.getElementById("contentT");
    editor.setTheme("ace/theme/textmate");
    editor.getSession().setMode("ace/mode/javascript");
	textarea.style.display = "none";
	editor.getSession().setValue(textarea.value);
</script>

<h2> API: </h2>

	<p>
		<h3>Defining a function:</h3>
		use <pre> Subscribe(string trigger, function(source, line, params) handler) </pre> to define a function. <br />
		The following trigger types are defined:
		
		<ul>
			<li>!command - These are your bog standard irc commands</li>
			<li>privmsg - This will trigger on all messages received</li>
			<li>join - Triggers if someone joins the channel</li>
			<li>part - Triggers when someone leaves the channel</li>
			<li>quit - Triggers when someone disconnects from irc</li>
			<li>regex: - Type a regex on which it will trigger after the colon (:)</li>
			<li>verb: - Type a verb which will trigger like "botname: verb"</li>
		</ul>
		
		The handler function has the following parameters:
		
		<ul>
			<li>source - This is a structure with the following members:
				<ul>
					<li>Nick - the sender's nick</li>
					<li>Source - Either the channel the message was sent on or the nick of the user if it was a private message</li>
					<li>Channel - Either the channel the message was sent on or the main channel if it was a private message</li>
				</ul>
			</li>
			<li>line - Either the complete message or the part after the !command</li>
			<li>params - In !commands this is a array of space delimited parameters. Parameters with a space in it can be consolidated with quotes. <br />
				<pre>!command param param21 "pa sdf asdfj dflk"</pre>
				is THREE parameters. 
				<ol>
					<li><pre>param</pre></li>
					<li><pre>param21</pre>and</li>
					<li><pre>pa sdf asdfj dflk</pre></li>
				<ol>
				Actual quotes can be escaped using \. Matching quotes will otherwise be removed.
			</li>
		</ul>	
			
	</p>

	<p>
		<h3>Function definitions</h3>
		
		<ul>
			<li>IRC
				<ul>
					<li>IRC.Privmsg(destination, message) - sends an IRC message to a channel or a nick</li>
					<li>IRC.Action(channel, message) - sends an "action" to a IRC channel</li>
					<li>IRC.Notice(nick, message) - sends a Notice towards a user</li>
					<li>IRC.Join(channel) - joins a channel</li>
					<li>IRC.Part(channel) - parts from a channel</li>
					<li>IRC.ChangeNick(nick) - changes the nick of the bot</li>
					<li>IRC.Channel - Contains the main channel of the bot</li>
					<li>IRC.Server - Contains the current server name</li>
					<li>IRC.Nick - Contains the nick of the bot</li>
					<li>IRC.DCCSend(nick, filename) - Sends a DCC file from the primary DCC file collection (see config)</li>
				</ul>
			</li>
			<li>
				DB
				<ul>
					<li>DB.Authenticate(user, pwd) - Authenticates against the user database</li>
					<li>DB.SaveToDb</li>
					<li>DB.UpdateInDB</li>
					<li>DB.ExistsInDB</li>
					<li>DB.GetFromDB</li>
					<li>DB.GetRandomFromDB</li>
					<li>DB.GetAndDeleteFirstFromDB</li>
					<li>DB.GetNamedFromDB</li>
					<li>DB.SaveNamedToDB</li>
					<li>DB.DeleteFromDB</li>
					<li>DB.Reconnect</li>
					<li>DB.LastError</li>
				</ul>
			</li>
			<li>
				Lib
				<ul>
					<li>Lib.HttpGet(Address) - Gets a http resource, returns a Response Object: <br />
						Strings: Body, Statusstring, Status <br /> 
						Object: Header</li>
					<li>Lib.IsAuthenticated(Nick) - Checks if the nick is authenticated on the current network</li>
					<li>Lib.GelbooruGet</li>
				</ul>
			</li>
			<li>
				SMS
				<ul>
					<li>SMS.Send(number, text) - Sends a SMS to the given number and text (Germany only) </br>
						Returns a error number and the SMS ID for the Status method if applicable, both in one string.</li>
					<li>SMS.Balance() - Gets the current SMS77 credit in Euros and cents</li>
					<li>SMS.Status(smsid) - Gets the SMS status (sent, waiting for cellphone to be on, etc...) </li>
					<li>SMS.Flipdebug() - Flips the debug switch (SMS are actually sent or not) and returns the new state</li>
					<li>SMS.GetPhonebook(id, nick, phonenumber, email) - Searches the Phonebook with the given parameters. Empty = not searched for</li>
					<li>SMS.SetPhonebook(id, nick, phonenumber, email) - Sets a phonebook entry or creates it (depending on id parameter. Empty = new entry)</li>
					<li>SMS.DelPhonebook(id) - Deletes an entry from the phone book.</li>
				<ul>
		</ul>
	</p>