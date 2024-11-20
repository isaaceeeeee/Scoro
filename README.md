<h1><b>Scoro Integration Tools</b></h1>
<p>This repository contains scripts and tools for automating tasks and integrating data with the Scoro API. The primary focus is on simplifying project and invoice management, improving data consistency, and enhancing workflow efficiency.</p>
<hr>
<h2><b>Features</b></h2>
<h3><b>Invoice Automation</b></h3>
<p>Retrieves, processes, and exports invoice data efficiently.</p>
<h3><b>Project Mapping</b></h3>
<p>Maps project IDs and names to ensure accurate system alignment.</p>
<h3><b>Custom Reporting</b></h3>
<p>Generates Excel reports for project tracking and financial analysis.</p>
<hr>
<h2><b>Installation</b></h2>
<h3><b>Clone this repository:</b></h3>
<p>bash</p>
<pre>
<code>git clone https://github.com/isaaceeeeee/Scoro.git</code>
</pre>
<h3><b>Install dependencies:</b></h3>
<p style="color: yellow;">bash</p>
<pre>
<code>pip install -r requirements.txt</code>
</pre>
<hr>
<h2><b>Usage (Python)</b></h2>
<h3><b>1. API Configuration</b></h3>
<p>Update the <code>config.json</code> file with your Scoro API credentials:</p>
<p style="color: red;">json</p>
<pre>
{
  "base_url" : "https://your_site.scoro.com/api/v2/",
  "api_key": "your_api_key",
  "company_account_id": "your_company_account_id"
  "lang": "eng",
}
</code>
</pre>
<h3><b>2. Run Scripts</b></h3>
<p>Run individual scripts depending on your task:</p>
<pre>
<code>python invoices.py</code>
</pre>
<hr>
<h2><b>Usage (VBA)</b></h2>
<h3><b>1. JSONify Code</b></h3>
<h3><b>2. Create Macro Environment</b></h3>
<hr>
<h2><b>Folder Structure</b></h2>
<ul>
<li><b>scripts/</b>: Core automation scripts.</li>
<li><b>data/</b>: Example input/output files.</li>
<li><b>docs/</b>: Additional documentation.</li>
</ul>
<hr>
<h2><b>Roadmap</b></h2>
<ul>
<li>Add real-time status updates for tasks.</li>
<li>Expand functionality to other Scoro modules.</li>
</ul>
<hr>
<h2><b>Contributing</b></h2>
<p>Contributions are welcome! Submit an issue or pull request to propose changes or suggest new features.</p>
<hr>
<h2><b>License</b></h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
