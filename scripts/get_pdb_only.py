import argparse
import os
import shutil
from tqdm import tqdm


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--design_pdb_dir', type=str, nargs='+', default=None, help='List of design PDB directories')
    parser.add_argument('--output_pdb_dir', default=None, help='Output PDB directory')
    parser.add_argument('--output_prefix', default=None, help='Output prefix')
    parser.add_argument('--no_renumber', action='store_true', help='No renumber')
    args = parser.parse_args()

    os.makedirs(args.output_pdb_dir, exist_ok=True)
    if not args.no_renumber:
        new_pdb_num = 0
        for design_pdb_path in tqdm(args.design_pdb_dir):
            pdb_files = os.listdir(design_pdb_path)
            pdb_files = [pdb_file for pdb_file in pdb_files if pdb_file.endswith('.pdb')]
            for pdb_file in tqdm(pdb_files):
                if args.output_prefix is not None:
                    new_pdb_name = f'{args.output_prefix}_{new_pdb_num}.pdb'
                else:
                    new_pdb_name = f'{new_pdb_num}.pdb'
                shutil.copy(os.path.join(design_pdb_path, pdb_file), os.path.join(args.output_pdb_dir, new_pdb_name))
                new_pdb_num += 1
        print(f'Renumbered {new_pdb_num} PDB files')
    else:
        total_pdb_num = 0
        for design_pdb_path in tqdm(args.design_pdb_dir):
            pdb_files = os.listdir(design_pdb_path)
            pdb_files = [pdb_file for pdb_file in pdb_files if pdb_file.endswith('.pdb')]
            for pdb_file in tqdm(pdb_files):
                shutil.copy(os.path.join(design_pdb_path, pdb_file), os.path.join(args.output_pdb_dir, pdb_file))
                total_pdb_num += 1
        print(f'Copied {total_pdb_num} PDB files')