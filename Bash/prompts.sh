declare -A symbols
symbols=(["09"]="🍩🍵" ["07"]="🌅" ["08"]="🌅" [10]="💻" [11]="💻" [12]="🍔🍟" [13]="🍔🍟" [14]="💻" [15]="💻" [16]="💻" [17]="🚗" [18]="🚗" [19]="🍷🍸" [20]="🍷🍸" [24]="🌙")
u_symbols() {
  c=${symbols[`date +"%H"`]}
  if [[ $c == "" ]]; then
    c=${symbols[24]}
  fi
  PS1='\u@\h:\w${c} '
};
u_symbols
export PROMPT_COMMAND="u_symbols;"
