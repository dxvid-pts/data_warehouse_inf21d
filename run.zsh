echo "Code-Formatierung durchführen"
          black .
          echo "Code-Formatierung abgeschlossen"
          #git config --global user.name 'github-actions'
         # git config --global user.email 'github-actions@github.com'
          git add -A
          echo "Checking for formatting changes"
          # Allow this command to fail without stopping the workflow
          git diff --exit-code

        # Capture the exit code
exit_code=$?

# You can now use the exit_code variable as needed
echo "The exit code is $exit_code"
          git diff --exit-code || true
          echo "checked for formatting changes"
          if [ $? -ne 0 ]; then
            echo "Code-Formatierung notwendig"
           # git commit -m "[AUTOMATED CHANGE] Code formatting"
            #git push
          else
            echo "Keine Formatierungsänderungen notwendig."
          fi