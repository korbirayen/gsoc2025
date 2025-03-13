import os
import pandas as pd


try:
    import pandas as pd
except ImportError:
    print("Installing pandas...")
    os.system("pip install pandas")


csv_file = "GSoc2025.csv" #Your CSV flie goes Here

if not os.path.exists(csv_file):
    print(f"Error: CSV file '{csv_file}' not found.")
    exit(1)

df = pd.read_csv(csv_file)


required_columns = ['Organizations']  # Adjust column names if necessary
for col in required_columns:
    if col not in df.columns:
        print(f"Error: Missing column '{col}' in CSV.")
        print("Available columns:", df.columns)
        exit(1)


output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Generate HTML files
for _, row in df.iterrows():
    org_name = str(row['Organizations']).strip().replace(" ", "_")  # Replace spaces with underscores
    filename = f"{output_dir}/{org_name}.html"
    
    # Fix potential invalid characters
    filename = filename.replace("\r", "").replace("\n", "")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"""
        <html>
        <head>
            <title>{row['Organizations']}</title>
            <link rel="stylesheet" href="/styles/organization_style.css">
        </head>
        <body>
            <a href="/index.html" class="back-button">Back to Home</a>
            <h1>{row['Organizations']}</h1>
            <p><strong>Slogan:</strong> {row['slogan']}</p>
            <p><strong>Tech Stack:</strong> {row['tech']}</p>
            <p><strong>Topic:</strong> {row['topic']}</p>
            <p><strong>Description:</strong> {row['descripton']}</p>
            <p><a href="{row['website']}">Website</a></p>
            <p><a href="{row['link']}">Link</a></p>
            <p><a href="{row['ideas']}">Project Ideas</a></p>
        </body>
        </html>
        """)

print("HTML pages generated successfully!")
