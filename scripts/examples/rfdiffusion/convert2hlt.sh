base_dir=data/IL13-VHH_Info/VHH5
poetry run python scripts/util/chothia2HLT.py \
    --input_pdb ${base_dir}/IL13_Chothia.pdb \
    --output ${base_dir}/IL13_Chothia_HLT.pdb \
    --heavy H